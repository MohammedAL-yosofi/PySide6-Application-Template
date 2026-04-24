"""
Application Settings Manager.

Reads and writes application configuration from settings.json.
"""

import json
import os


class Settings:
    """Manages application settings loaded from settings.json."""

    _json_file = "settings.json"
    _app_path = os.path.abspath(os.getcwd())
    _settings_path = os.path.normpath(os.path.join(_app_path, _json_file))

    if not os.path.isfile(_settings_path):
        print(f'WARNING: "settings.json" not found! Check in: {_settings_path}')

    def __init__(self):
        self.items: dict = {}
        self._deserialize()

    def __getitem__(self, key):
        """Allow dict-style access: settings['app_name']."""
        return self.items[key]

    def serialize(self) -> None:
        """Write current settings to JSON file."""
        with open(self._settings_path, "w", encoding="utf-8") as f:
            json.dump(self.items, f, indent=4)

    def _deserialize(self) -> None:
        """Read settings from JSON file."""
        with open(self._settings_path, "r", encoding="utf-8") as f:
            self.items = json.loads(f.read())
