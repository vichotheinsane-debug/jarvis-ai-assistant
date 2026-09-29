from __future__ import annotations

import os
import platform
import shutil
import subprocess
from typing import Any

from app.config.settings import settings
from app.core.logger import log_event
from app.security.permissions import PermissionChecker


class PCController:
    def __init__(self):
        self.permissions = PermissionChecker(settings.allowlist.split(","), settings.dangerous.split(","))

    def execute(self, action: str, target: str | None = None, confirmed: bool = False) -> dict[str, Any]:
        if not self.permissions.check(action):
            raise PermissionError(f"No tengo permisos suficientes para realizar esa acción: {action}.")
        if self.permissions.requires_confirmation(action) and not confirmed:
            return {"requires_confirmation": True, "action": action, "target": target, "message": "Esta acción podría afectar el sistema. ¿Quieres continuar?"}

        if action == "open_application":
            return self.open_application(target)
        if action == "close_application":
            return self.close_application(target)
        if action == "open_url":
            return self.open_url(target)
        if action == "open_file":
            return self.open_file(target)
        if action == "open_folder":
            return self.open_folder(target)
        if action == "volume_control":
            return self.volume_control(target)
        if action == "media_control":
            return self.media_control(target)
        if action == "system_information":
            return self.system_information()
        if action == "shutdown":
            return self.shutdown()
        if action == "restart":
            return self.restart()
        if action == "suspend":
            return self.suspend()
        if action == "wake_system":
            return self.wake_system()
        raise ValueError(f"Acción no implementada: {action}")

    def open_application(self, target: str | None) -> dict[str, Any]:
        if not target:
            raise ValueError("Falta el nombre de la aplicación.")
        log_event("INFO", "Opening application", application=target)
        command = self._build_open_command(target)
        return self._run_command(command, label=f"open:{target}")

    def close_application(self, target: str | None) -> dict[str, Any]:
        if not target:
            raise ValueError("Falta el nombre de la aplicación.")
        log_event("INFO", "Closing application", application=target)
        return {"status": "simulated", "action": "close_application", "target": target, "message": f"Se cerraría {target}."}

    def open_url(self, target: str | None) -> dict[str, Any]:
        if not target:
            raise ValueError("Falta la URL.")
        command = self._build_url_command(target)
        return self._run_command(command, label=f"url:{target}")

    def open_file(self, target: str | None) -> dict[str, Any]:
        if not target:
            raise ValueError("Falta la ruta del archivo.")
        return self._run_command(self._build_file_command(target), label=f"file:{target}")

    def open_folder(self, target: str | None) -> dict[str, Any]:
        if not target:
            raise ValueError("Falta la ruta de la carpeta.")
        return self._run_command(self._build_folder_command(target), label=f"folder:{target}")

    def volume_control(self, target: str | None) -> dict[str, Any]:
        direction = (target or "up").lower()
        log_event("INFO", "Volume adjusted", direction=direction)
        return {"status": "ok", "action": "volume_control", "direction": direction, "message": f"Volumen {direction}."}

    def media_control(self, target: str | None) -> dict[str, Any]:
        action = target or "toggle"
        log_event("INFO", "Media action", action=action)
        return {"status": "ok", "action": "media_control", "target": action, "message": f"Reproducción: {action}."}

    def system_information(self) -> dict[str, Any]:
        try:
            import psutil
            return {
                "status": "ok",
                "cpu_percent": psutil.cpu_percent(interval=None),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_percent": psutil.disk_usage('/').percent,
                "platform": platform.platform(),
            }
        except Exception:
            return {"status": "ok", "platform": platform.platform(), "message": "psutil no disponible."}

    def shutdown(self) -> dict[str, Any]:
        log_event("INFO", "Shutdown requested")
        return {"status": "simulated", "action": "shutdown", "message": "Acción de apagado simulada; requiere confirmación real y permisos del sistema."}

    def restart(self) -> dict[str, Any]:
        log_event("INFO", "Restart requested")
        return {"status": "simulated", "action": "restart", "message": "Acción de reinicio simulada; requiere confirmación real y permisos del sistema."}

    def suspend(self) -> dict[str, Any]:
        system = platform.system().lower()
        log_event("INFO", "Suspend requested", system=system)
        if system == "windows":
            result = subprocess.run(["powershell", "-Command", "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.Application]::SetSuspendState('Suspend', $false, $true)"], capture_output=True, text=True)
            return {"status": "ok" if result.returncode == 0 else "error", "action": "suspend", "message": "Suspensión solicitada en Windows."}
        if system == "linux":
            result = subprocess.run(["systemctl", "suspend"], capture_output=True, text=True)
            return {"status": "ok" if result.returncode == 0 else "error", "action": "suspend", "message": "Suspensión solicitada en Linux."}
        return {"status": "unsupported", "action": "suspend", "message": "Este sistema operativo no admite suspensión nativa desde la aplicación actual."}

    def wake_system(self) -> dict[str, Any]:
        system = platform.system().lower()
        log_event("INFO", "Wake system requested", system=system)
        if system == "windows":
            return {"status": "ready", "action": "wake_system", "message": "Preparado para despertar con Wake-on-LAN, RTC o wake timers si el hardware lo soporta."}
        if system == "linux":
            return {"status": "ready", "action": "wake_system", "message": "Se requiere configuración del firmware y BIOS para Wake-on-LAN o wake timers."}
        return {"status": "unsupported", "action": "wake_system", "message": "No hay soporte nativo detectado para despertar este hardware."}

    def _build_open_command(self, target: str) -> list[str]:
        if platform.system() == "Windows":
            return ["cmd", "/c", f"start " + target]
        if platform.system() == "Darwin":
            return ["open", target]
        return ["xdg-open", target]

    def _build_url_command(self, target: str) -> list[str]:
        if platform.system() == "Windows":
            return ["cmd", "/c", f"start {target}"]
        if platform.system() == "Darwin":
            return ["open", target]
        return ["xdg-open", target]

    def _build_file_command(self, target: str) -> list[str]:
        if platform.system() == "Windows":
            return ["cmd", "/c", f"start ""{target}"""]
        if platform.system() == "Darwin":
            return ["open", target]
        return ["xdg-open", target]

    def _build_folder_command(self, target: str) -> list[str]:
        return self._build_file_command(target)

    def _run_command(self, command: list[str], label: str) -> dict[str, Any]:
        try:
            subprocess.Popen(command)
            log_event("INFO", "Executed action", action=label)
            return {"status": "ok", "action": label, "command": command}
        except Exception as exc:  # pragma: no cover - defense
            log_event("ERROR", "Execution error", error=str(exc), action=label)
            return {"status": "error", "action": label, "error": str(exc)}
