import numpy as np
from typing import TypedDict, Callable


class Coordinates(TypedDict):
    x: str
    y: str


class Serializer:
    mapping = {
        "-": False,
        "o": True
    }

    @classmethod
    def sample_to_array(cls, sample: str) -> np.ndarray:
        """
        Converts binary string to array representation.
        """
        sample_cleaned = sample.replace(" ", "")
        sample_newlines = sample_cleaned.splitlines()
        sample_divided = [list(x) for x in sample_newlines]
        sample_array = np.array(sample_divided)
        sample_array = np.where(sample_array == "-", cls.mapping['-'], cls.mapping['o'])
        return sample_array

    @classmethod
    def array_to_sample(cls, array: np.ndarray) -> str:
        array_strings = np.where(array == True, "o", "-")
        array_strings = ["".join(x) for x in array_strings]
        strings = "\n".join(array_strings)
        return strings


def calculate_jaccard_similarity(x: np.ndarray, y: np.ndarray) -> float:
    """Calculates area over union for two arrays (x,y) with the same shape.
       :return: value from 0 (no similarity) to 1 (perfect similarity)
    """
    similarity = np.equal(x, y)
    return similarity.sum() / x.size


def convolve_array(kernel: np.ndarray, array: np.ndarray, aggregator: Callable = calculate_jaccard_similarity):
    kernel_shape_y, kernel_shape_x = kernel.shape
    array_shape_y, array_shape_x = array.shape
    array_results = np.zeros((array_shape_y - kernel_shape_y + 1, array_shape_x - kernel_shape_x + 1))
    for y in range(0, array_shape_y - kernel_shape_y + 1):
        for x in range(0, array_shape_x - kernel_shape_x + 1):
            array_slice = array[y:y + kernel_shape_y, x: x + kernel_shape_x]
            array_results[y, x] = aggregator(kernel, array_slice)
    return array_results
