"""Unit tests for entities code."""
from source.entities import Invader, Radar, RadarSample

from numpy.testing import assert_array_equal
import numpy as np
import pytest


@pytest.fixture
def invader():
    return Invader(np.array([[1, 1, 1],
                             [1, 1, 1],
                             [1, 1, 1]]))


@pytest.mark.parametrize("radar_sample, expected_coordinates, precision, error_message", [
    (np.array([[0, 1, 1, 1],
               [0, 1, 1, 1],
               [0, 1, 1, 1],
               [0, 0, 0, 0]]), [{"y": 0, "x": 1}], 1.0, "Invader fully visible."),

    (np.array([[0, 1, 1, 1],
               [0, 1, 0, 1],
               [0, 1, 1, 1],
               [0, 0, 0, 0]]), [{"y": 0, "x": 1}], 0.8, "Invader contains false negative."),

    (np.array([[1, 1, 1, 1],
               [0, 1, 1, 1],
               [0, 1, 1, 1],
               [1, 0, 0, 0]]), [{"y": 0, "x": 1}], 0.8, "Invader contains false positive."),

    (np.array([[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 1, 1, 1],
               [0, 1, 1, 1]]), [{"y": 1, "x": 1}, {"y": 2, "x": 1}], 0.6, "Invader partially visible"),

    (np.array([[0, 1, 1, 1, 0],
               [0, 1, 1, 1, 1],
               [0, 1, 1, 1, 1],
               [0, 0, 1, 1, 1]]), [{"y": 0, "x": 1}, {"y": 1, "x": 2}], 1.0, "Invaders overlap on each other."),
])
def test_invader_detection(invader, radar_sample, precision, expected_coordinates, error_message):
    """Tests different scenarios"""
    radar_sample = RadarSample(appearance=radar_sample)
    radar_reading = Radar(invader, radar_sample, precision)
    radar_reading.locate_invader()
    assert_array_equal(radar_reading.invader_coordinates, expected_coordinates), error_message
