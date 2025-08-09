def print_splash_text(WHITE: str, BLUE: str, RESET: str, color: bool) -> None:
    fg, bg = (f"{WHITE}▓{RESET}", f"{BLUE}▓{RESET}") if color else (f"#", f".")

    splash = f"""
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
"""

    print(splash)

def print_splash_text_background(color: bool) -> None:
    BLUE = "\033[44m"
    WHITE = "\033[47m"
    RESET = "\033[0m"

    fg, bg = (f"{WHITE} {RESET}", f"{BLUE} {RESET}") if color else (f"#", f".")

    splash = f"""
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{fg}{fg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}{bg}
"""

    print(splash)