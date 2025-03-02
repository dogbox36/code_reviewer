from backend.code_analyzer import analyze_code

def test_analyze_code():
    code = "print('Hello, World!')"
    response = analyze_code(code)
    assert "print" in response  # Ellenőrizzük, hogy feldolgozta-e
