import subprocess

def run_pylint(code_file: str):
    """Futtatja a pylint-et és visszaadja az eredményt."""
    result = subprocess.run(["pylint", code_file], capture_output=True, text=True)
    return result.stdout

def run_flake8(code_file: str):
    """Futtatja a flake8-at és visszaadja az eredményt."""
    result = subprocess.run(["flake8", code_file], capture_output=True, text=True)
    return result.stdout
