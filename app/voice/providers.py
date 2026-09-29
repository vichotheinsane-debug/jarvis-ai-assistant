from __future__ import annotations

from app.core.logger import log_event
from app.pc_control.actions import PCController


class RoutineManager:
    def __init__(self):
        self.pc = PCController()

    def trigger_night_mode(self) -> dict[str, str]:
        log_event("INFO", "Night mode activated")
        # Close/park applications here as configuration-driven behavior.
        result = self.pc.suspend()
        return {"status": result.get("status", "ok"), "message": "Modo nocturno activado."}

    def trigger_morning_routine(self) -> dict[str, str]:
        log_event("INFO", "Morning routine triggered")
        return {"status": "ok", "message": "Rutina de buenos días ejecutada."}

    def stop_all_automations(self) -> dict[str, str]:
        log_event("WARNING", "All automations stopped")
        return {"status": "stopped", "message": "Todas las automatizaciones han sido detenidas."}
