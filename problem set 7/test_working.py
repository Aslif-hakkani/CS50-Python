import pytest
from working import convert


def test_basic():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_optional_minutes():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"


def test_am_pm():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:30 AM to 12:30 PM") == "00:30 to 12:30"
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"


def test_invalid_time():
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

    with pytest.raises(ValueError):
        convert("9 AM to 5")

    with pytest.raises(ValueError):
        convert("9:00 to 17:00")
