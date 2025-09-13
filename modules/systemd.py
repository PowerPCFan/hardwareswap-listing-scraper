from modules.colors.ansi_codes import RESET, RED, GREEN, YELLOW, CYAN


class Logger:
    def __init__(self) -> None:
        pass

    def ok(self, message: str) -> None:
        print(f"[{GREEN} OK {RESET}] {message}")

    def failed(self, message: str) -> None:
        print(f"[{RED} FAILED {RESET}] {message}")

    def warn(self, message: str) -> None:
        print(f"[{YELLOW} WARN {RESET}] {message}")

    def info(self, message: str) -> None:
        print(f"[{CYAN} INFO {RESET}] {message}")
