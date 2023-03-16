"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest


# def test_daily_mean_zeros():
#     """Test that mean function works for an array of zeros."""
#     from inflammation.models import daily_mean
#
#     test_input = np.array([[0, 0],
#                            [0, 0],
#                            [0, 0]])
#     test_result = np.array([0, 0])
#
#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(daily_mean(test_input), test_result)
#
#
# def test_daily_mean_integers():
#     """Test that mean function works for an array of positive integers."""
#     from inflammation.models import daily_mean
#
#     test_input = np.array([[1, 2],
#                            [3, 4],
#                            [5, 6]])
#     test_result = np.array([3, 4])
#
#     # Need to use Numpy testing functions to compare arrays
#     npt.assert_array_equal(daily_mean(test_input), test_result)


@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
    ])

def test_daily_mean(test,expected):
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))


# def test_daily_max():
#     """ Testing the max value with positive integers"""
#     from inflammation.models import daily_max
#
#     test_input = np.array([[7, 8, 9],
#                            [1, 2, 3],
#                            [3, 4, 5]])
#
#     test_result = np.array([7, 8, 9])
#
#     npt.assert_array_equal(daily_max(test_input), test_result)


@pytest.mark.parametrize(
    "test,expected",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [0, 0, 0]),
        ([[4, 2, 5], [1, 6, 2], [4, 1, 9]], [4, 6, 9]),
        ([[4, -2, 5], [1, -6, 2], [-4, -1, 9]], [4, -1, 9]),
    ])

def test_daily_max(test,expected):
    """ Testing the max value with positive integers"""
    from inflammation.models import daily_max

    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
    "test,expected",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [0, 0, 0]),
        ([[4, 2, 5], [1, 6, 2], [4, 1, 9]], [1, 1, 2]),
        ([[4, -2, 5], [1, -6, 2], [-4, -1, 9]], [-4, -6, 2]),
    ])

def test_daily_min(test,expected):
    """Testing the daily minimum using positive and negative integers"""
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))


def test_daily_minimum_string():
    """ Tesing for type errors when passing in strings"""
    from inflammation.models import daily_min
    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])





@pytest.mark.parametrize(
    "test,expected",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [0, 0, 0]),
        ([[1, 0, 100], [2, 0, 1], [3, 0, 50]], [0.82, 0, 40.41]),

    ])
def test_dayly_std(test, expected):

    from inflammation.models import daily_add_std

    npt.assert_array_almost_equal(daily_add_std(np.array(test)), np.array(expected), decimal=2)