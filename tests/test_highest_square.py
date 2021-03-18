import pytest

from beginner.highest_square import highest_square


def test_highest_square_example():
    assert highest_square(500) == 484

def test_invalid():
    assert highest_square(0) == None
