import os
import sys
import ctypes
import functools

def ansi_codes():
    ANSI = "\033["
    RESET = f"{ANSI}0m"
    RED = f"{ANSI}31m"
    GREEN = f"{ANSI}32m"
    BLUE = f"{ANSI}34m"
    YELLOW = f"{ANSI}33m"
    WHITE = f"{ANSI}37m"
    PURPLE = f"{ANSI}35m"
    CYAN = f"{ANSI}36m"
    LIGHT_CYAN = f"{ANSI}96m"
    SUPER_LIGHT_CYAN = f"{ANSI}38;5;153m"
    ORANGE = f"{ANSI}38;5;208m"
    
    return RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE

# Thanks to ChatGPT for this, I modified it but the core logic is from chatgpt

def enable_ansi_windows():
    try:
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        mode = ctypes.c_uint()
        if not kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            return False
        new_mode = mode.value | 0x0004
        return kernel32.SetConsoleMode(handle, new_mode) != 0
    except Exception:
        return False

def supports_ansi(vt_enabled):
    if os.name != 'nt':
        return sys.stdout.isatty()
    
    if vt_enabled:
        return True

    return (
        sys.stdout.isatty() and (
            'ANSICON' in os.environ or
            'WT_SESSION' in os.environ or
            os.environ.get('TERM_PROGRAM') == 'vscode' or
            'TERM' in os.environ and 'xterm' in os.environ['TERM']
        )
    )

@functools.lru_cache(maxsize=None)
def ansi_supported():
    vt_enabled = False
    if os.name == 'nt':
        vt_enabled = enable_ansi_windows()
    
    if supports_ansi(vt_enabled):
        return True
    else:
        return False
