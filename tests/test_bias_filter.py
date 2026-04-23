import sys
sys.path.insert(0, "backend")

from services.bias_filter import (
    remove_gender_signals,
    remove_age_signals,
    remove_location_signals,
    apply_bias_filter
)

def test_gender_removal():
    text = "He is a great developer. She managed a team."
    result = remove_gender_signals(text)
    assert "He" not in result
    assert "She" not in result
    print("✅ Gender removal test passed!")

def test_age_removal():
    text = "Graduated in 2001 with a degree in Computer Science"
    result = remove_age_signals(text)
    assert "2001" not in result
    print("✅ Age removal test passed!")

def test_location_removal():
    text = "Contact: john@email.com Phone: +1-555-0101"
    result = remove_location_signals(text)
    assert "john@email.com" not in result
    assert "+1-555-0101" not in result
    print("✅ Location removal test passed!")

def test_full_filter():
    text = "John Smith, john@email.com, He graduated in 2001"
    result = apply_bias_filter(text)
    assert "john@email.com" not in result
    assert "2001" not in result
    print("✅ Full bias filter test passed!")