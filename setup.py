import sys
from cx_Freeze import setup, Executable
import os.path
from pynput.keyboard import Listener

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["pynput", "pynput.keyboard", "pymsgbox", "PIL"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
#if sys.platform == "win32":
    #base = "Win32GUI"

setup(
    name="MacroEmpire",
    version="0.1",
    description="MacroEmpire",
    options={"build_exe": build_exe_options},
    executables=[Executable("joao.py", base=base, icon="icone.ico")]
)

