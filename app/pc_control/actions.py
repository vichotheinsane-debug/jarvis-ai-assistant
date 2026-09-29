from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any


@dataclass
class CommandIntent:
    intent: str
    action: str
    target: str | None = None
    confirmation_required: bool = False
    response: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


class IntentRouter:
    def route(self, text: str) -> CommandIntent:
        message = (text or "").strip().lower()
        if not message:
            return CommandIntent(intent="unknown", action="noop", response="No entendí el comando.")

        if re.search(r"(buenas?\s*noches|modo nocturno|me voy a dormir)", message):
            return CommandIntent(
                intent="night_mode",
                action="suspend",
                response="Buenas noches, señor Vicho. Activando modo nocturno y suspendiendo el sistema.",
                confirmation_required=False,
                metadata={"sleep_mode": True},
            )

        if re.search(r"(buenos?\s*d[ií]as|despiertate|despertar)", message):
            return CommandIntent(
                intent="morning_routine",
                action="wake_system",
                response="Buenos días, señor Vicho. El sistema está nuevamente en línea.",
                metadata={"wake": True},
            )

        if re.search(r"(abrir|abre|lanzar|ejecutar)\s+(.*)", message):
            target = re.sub(r"(abrir|abre|lanzar|ejecutar|puedes|por favor|señor)\s+", "", message)
            if target:
                return CommandIntent(
                    intent="open_application",
                    action="open_application",
                    target=target.strip(),
                    response=f"Claro, señor Vicho. Abriendo {target.strip()}.",
                )

        if re.search(r"(cerrar|cierra)\s+(.*)", message):
            target = re.sub(r"(cerrar|cierra|por favor|señor)\s+", "", message)
            return CommandIntent(
                intent="close_application",
                action="close_application",
                target=target.strip(),
                response=f"Cerrando {target.strip()}.",
            )

        if re.search(r"(hora|qué hora|que hora)", message):
            return CommandIntent(intent="time", action="get_time", response="Consultando la hora del sistema.")

        if re.search(r"(tiempo|clima|weather)", message):
            return CommandIntent(intent="weather", action="check_weather", response="Consultando el clima.")

        if re.search(r"(volumen|sube|baja)", message):
            return CommandIntent(intent="volume", action="volume_control", response="Ajustando el volumen.", metadata={"direction": "up" if "sube" in message else "down"})

        if re.search(r"(música|musica|play|pause|pausa)", message):
            return CommandIntent(intent="media", action="media_control", response="Controlando la reproducción multimedia.")

        if re.search(r"(reinicia|reiniciar|restart)", message):
            return CommandIntent(
                intent="restart",
                action="restart",
                response="Esto reiniciará el equipo. ¿Quieres continuar?",
                confirmation_required=True,
            )

        if re.search(r"(apaga|apagar|shutdown)", message):
            return CommandIntent(
                intent="shutdown",
                action="shutdown",
                response="Esto apagará el equipo. ¿Quieres continuar?",
                confirmation_required=True,
            )

        if re.search(r"(ayuda|qué puedes hacer|que puedes hacer)", message):
            return CommandIntent(
                intent="help",
                action="help",
                response="Puedo abrir aplicaciones, controlar volumen, consultar clima, manejar recordatorios y ejecutar rutinas de buena mañana y noche.",
            )

        if re.search(r"(recuerda|recordatorio|recuérdame)", message):
            return CommandIntent(intent="reminder", action="set_reminder", response="Guardaré ese recordatorio.")

        if re.search(r"(buscar|busca|investiga)", message):
            target = re.sub(r"(buscar|busca|investiga|por favor|señor)\s+", "", message)
            return CommandIntent(intent="search", action="search_web", target=target.strip(), response=f"Buscando información sobre {target.strip()}.")

        if re.search(r"(estado|systema|cpu|ram|memoria|almacenamiento)", message):
            return CommandIntent(intent="system_information", action="system_information", response="Revisando el estado del sistema.")

        return CommandIntent(intent="unknown", action="noop", response="No tengo configurado ese servicio todavía.")
