from modules.ansi import ansi_supported, ansi_codes
import subprocess
import sys

RESET, RED, GREEN, BLUE, YELLOW, WHITE, PURPLE, CYAN, LIGHT_CYAN, SUPER_LIGHT_CYAN, ORANGE = ansi_codes() if ansi_supported() else ("",) * 11

class Logger:
    def __init__(self):
        pass

    def ok(self, message):
        print(f"[{GREEN} OK {RESET}] {message}")

    def failed(self, message):
        print(f"[{RED} FAILED {RESET}] {message}")
        
def check_dependencies():
    logger = Logger()

    # Get dependencies from requirements.txt
    try:
        with open("requirements.txt", "r") as f:
            dependencies = {}
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    parts = line.split("==")
                    name = parts[0]
                    version = parts[1] if len(parts) > 1 else None
                    dependencies[name] = version
    except FileNotFoundError:
        logger.failed("requirements.txt not found. Please ensure it exists in the current directory.")
        return
    except Exception as e:
        logger.failed(f"Error reading requirements.txt: {e}")
        return

    for dep, version in dependencies.items():
        try:
            __import__(dep)
            logger.ok(f"{dep} version {version} is installed.")
        except ImportError:
            logger.failed(f"{dep} is not installed. Installing...")
            try:
                install_str = f"{dep}=={version}" if version else dep
                subprocess.check_call([sys.executable, "-m", "pip", "install", install_str])
            except Exception as e:
                logger.failed(f"Failed to install {dep} version {version}. Error message: {e}\nPlease install it manually using the command: pip install {install_str}")
                continue
        except Exception as e:
            logger.failed(f"An error occurred while checking if {dep} is installed: {e}")
            continue