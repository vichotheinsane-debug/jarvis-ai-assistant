from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class PluginDefinition:
    name: str
    description: str
    permissions: list[str] = field(default_factory=list)
    commands: list[str] = field(default_factory=list)
    config: dict[str, str] = field(default_factory=dict)
    enabled: bool = True


class PluginManager:
    def __init__(self):
        self.plugins = {
            "weather": PluginDefinition(
                name="weather",
                description="Consulta meteorológica por API externa.",
                permissions=["weather"],
                commands=["qué tiempo hace", "clima"],
                config={"provider": "openweathermap"},
            ),
            "spotify": PluginDefinition(
                name="spotify",
                description="Control de música y reproducción.",
                permissions=["media_control"],
                commands=["pon música", "pausa"],
                config={"client_id": ""},
            ),
            "discord": PluginDefinition(
                name="discord",
                description="Acceso a notificaciones y controles del cliente Discord.",
                permissions=["notifications"],
                commands=["lee mis notificaciones"],
                config={"enabled": "false"},
            ),
            "pc": PluginDefinition(
                name="pc",
                description="Estado del equipo y automatización local.",
                permissions=["system_information", "volume_control"],
                commands=["estado del pc", "cpu", "ram"],
                config={"safe_mode": "true"},
            ),
        }

    def list_plugins(self) -> list[dict[str, object]]:
        return [
            {
                "name": plugin.name,
                "description": plugin.description,
                "permissions": plugin.permissions,
                "commands": plugin.commands,
                "enabled": plugin.enabled,
            }
            for plugin in self.plugins.values()
        ]

    def get(self, name: str) -> PluginDefinition | None:
        return self.plugins.get(name)
