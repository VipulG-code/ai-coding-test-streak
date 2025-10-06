"""Tests for streak.py"""
import pytest
from streak import longest_positive_streak


def test_empty_input():
    """Empty list should return 0."""
    assert longest_positive_streak([]) == 0


def test_all_positive():
    """All positive numbers should return the full length."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5


def test_all_negative():
    """All negative numbers should return 0."""
    assert longest_positive_streak([-1, -2, -3, -4]) == 0


def test_all_zeros():
    """All zeros should return 0."""
    assert longest_positive_streak([0, 0, 0, 0]) == 0


def test_multiple_streaks_longest_wins():
    """Multiple streaks: longest should win."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3
    assert longest_positive_streak([1, 2, -1, 3, 4, 5, 6]) == 4


def test_zeros_break_streak():
    """Zeros should break the streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3


def test_negatives_break_streak():
    """Negative numbers should break the streak."""
    assert longest_positive_streak([1, 2, -5, 3, 4]) == 2


def test_mixed_zeros_and_negatives():
    """Mix of zeros and negatives breaking streaks."""
    assert longest_positive_streak([1, 2, 0, 3, -1, 4, 5, 6]) == 3


def test_repeated_values():
    """Repeated positive values should count as a streak."""
    assert longest_positive_streak([1, 1, 1]) == 3
