from um import count


def test_basic():
    assert count("um") == 1
    assert count("hello, um, world") == 1
    assert count("um, um") == 2


def test_case_insensitive():
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("Um, thanks, UM...") == 2


def test_punctuation():
    assert count("um?") == 1
    assert count("um!") == 1
    assert count("(um)") == 1
    assert count("um, um...") == 2


def test_not_substring():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("album") == 0
    assert count("human") == 0


def test_multiple():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("um um um um") == 4
