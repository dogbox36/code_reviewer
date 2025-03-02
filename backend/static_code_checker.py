import subprocess
import os

def run_pylint(code_file: str):
    """Futtatja a pylint-et és visszaadja az eredményt."""
    if not os.path.exists(code_file):
        return "⚠️ Hiba: A fájl nem létezik!"

    result = subprocess.run(["pylint", code_file], capture_output=True, text=True)
    return result.stdout

def run_flake8(code_file: str):
    """Futtatja a flake8-at és visszaadja az eredményt."""
    if not os.path.exists(code_file):
        return "⚠️ Hiba: A fájl nem létezik!"
        
    result = subprocess.run(["flake8", code_file], capture_output=True, text=True)
    return result.stdout
