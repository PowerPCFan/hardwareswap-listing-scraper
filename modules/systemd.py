from modules.colors.ansi_codes import RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE, ansi_is_supported

class Logger:
    def __init__(self):
        pass

    def ok(self, message):
        print(f"[{GREEN} OK {RESET}] {message}")

    def failed(self, message):
        print(f"[{RED} FAILED {RESET}] {message}")
        
    def warn(self, message):
        print(f"[{YELLOW} WARN {RESET}] {message}")
    
    def info(self, message):
        print(f"[{CYAN} INFO {RESET}] {message}")