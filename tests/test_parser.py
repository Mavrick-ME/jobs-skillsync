import sys
sys.path.insert(0, "backend")

from services.parser import parse_txt

def test_parse_txt():
    # Create a temp txt file and test parsing
    import tempfile, os
    content = "John Smith\nPython Developer\nSkills: Python, FastAPI"
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(content)
        path = f.name

    result = parse_txt(path)
    os.unlink(path)

    assert "Python" in result
    assert "John Smith" in result
    assert len(result) > 0
    print("✅ Parser test passed!")

def test_parse_empty():
    import tempfile, os
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("")
        path = f.name

    result = parse_txt(path)
    os.unlink(path)
    assert result == ""
    print("✅ Empty file test passed!")