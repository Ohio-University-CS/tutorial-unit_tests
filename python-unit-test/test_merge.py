from calculator import add, subtract, multiply, divide

def test_add():
    """Verify addition works for positive, negative, and zero."""
    assert add(3, 2) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    """Verify subtraction handles positive and negative results."""
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -4