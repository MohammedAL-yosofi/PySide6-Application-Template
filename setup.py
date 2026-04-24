"""
cx_Freeze build script for School Management System.

Usage:  python setup.py build
"""

import sys
from cx_Freeze import setup, Executable

# Files/folders to include in the build
files = ["icon.ico", "settings.json", "images/"]

target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico",
)

setup(
    name="SchoolMS",
    version="1.0",
    description="School Management System",
    author="Al-yoso",
    options={"build_exe": {"include_files": files}},
    executables=[target],
)
