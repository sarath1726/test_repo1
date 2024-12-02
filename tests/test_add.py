from drivers.add import add , sub , mul

def test_positive_numbers():
    """Test addition of two positive numbers."""
    result = add(2, 3)
    assert result == 5, f"Expected 5 but got {result}"

def test_negative_numbers():
    """Test addition of two negative numbers."""
    result = add(-2, -3)
    assert result == -5, f"Expected -5 but got {result}"


def test_sub_numbers():
    """Test addition of two positive numbers."""
    result = sub(4, 2)
    assert result == 2, f"Expected 2 but got {result}"


def test_mul_numbers():
    """Test addition of two positive numbers."""
    result = mul(4, 2)
    assert result == 8, f"Expected 8 but got {result}"
