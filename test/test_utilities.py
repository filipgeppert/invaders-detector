"""Unit tests for utilities code."""
from source.utilities import convolve_array, calculate_jaccard_similarity, Serializer

from numpy.testing import assert_array_equal
import numpy as np


class TestSerialization:
    def test_serialize_sample_to_array(self):
        sample = """--o\n-o-\n--o"""
        array = Serializer.sample_to_array(sample)
        assert_array_equal(array, np.array([[0, 0, 1], [0, 1, 0], [0, 0, 1]]))

    def test_deserialize_array_to_sample(self):
        sample_expected = """--o\n-o-\n--o"""
        array = np.array([[0, 0, 1], [0, 1, 0], [0, 0, 1]])
        sample = Serializer.array_to_sample(array)
        assert_array_equal(sample, sample_expected)


def test_jaccard_similarity():
    x = np.array([[0, 0], [1, 1]])
    y = np.array([[0, 1], [1, 1]])
    similarity = calculate_jaccard_similarity(x, y)
    assert np.round(similarity, 2) == 0.75


def test_convolve_array():
    kernel = np.array([[1, 1], [1, 1]])
    array = np.array([[1, 0, 1], [1, 1, 1], [0, 1, 1], [0, 0, 0]])
    results = convolve_array(kernel=kernel, array=array)
    assert_array_equal(results, np.array([[0.75, 0.75], [0.75, 1.0], [0.25, 0.5]]))
