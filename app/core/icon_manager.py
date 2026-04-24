"""
FontAwesome Icon Manager for PySide6.

Uses qtawesome to generate QIcon objects with caching.
Singleton pattern ensures a single shared icon cache.
"""

from typing import Optional

import qtawesome as qta
from PySide6.QtGui import QIcon


class IconManager:
    """Singleton icon manager with caching for FontAwesome icons."""

    _instance = None
    _cache = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IconManager, cls).__new__(cls)
        return cls._instance

    def get_icon(self, name: str, size: int = 20, color: str = "#ffffff") -> Optional[QIcon]:
        """
        Get a FontAwesome QIcon by name.

        Args:
            name:  FontAwesome icon name (e.g. 'fa5s.home', 'fa5s.cog').
            size:  Icon scale reference (pixels).
            color: Hex color string.

        Returns:
            QIcon or None if generation fails.
        """
        key = f"{name}_{size}_{color}"
        if key in self._cache:
            return self._cache[key]

        try:
            icon = qta.icon(name, color=color, scale_factor=1.0)
            self._cache[key] = icon
            return icon
        except Exception as e:
            print(f"Error generating icon '{name}': {e}")
            return None
