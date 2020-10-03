import numpy as np
from typing import List
from source.utilities import convolve_array, Coordinates


class Shape:
    def __init__(self, appearance: np.ndarray):
        self.appearance = appearance
        self.width = self.appearance.shape[1]
        self.height = self.appearance.shape[0]


class Invader(Shape):
    def __init__(self, appearance: np.ndarray):
        super().__init__(appearance)


class RadarSample(Shape):
    def __init__(self, appearance: np.ndarray):
        super().__init__(appearance)


class Radar:
    """Locates invader coordinates on a radar sample."""

    def __init__(self, invader: Invader, radar_sample: RadarSample, precision: float = 0.8, padding=10):
        self.invader = invader
        self._invader_locations = None
        self.invader_coordinates: List[Coordinates] = []
        self.radar_sample = radar_sample
        self.precision = precision
        self.results = np.zeros((self.radar_sample.height, self.radar_sample.width))
        self.pad_value = padding
        self._radar_sample_padded = np.pad(self.radar_sample.appearance,
                                           ((self.pad_value, self.pad_value),
                                            (self.pad_value, self.pad_value)),
                                           'constant')
        self._results_padded = np.zeros(self._radar_sample_padded.shape)

    def locate_invader(self):
        invader_locations = convolve_array(self.invader.appearance, self._radar_sample_padded)
        invader_locations = np.where(invader_locations >= self.precision, invader_locations, 0)
        self._invader_locations = invader_locations
        self.save_results()

    def save_results(self):
        location_coordinates = np.nonzero(self._invader_locations)
        for y, x in zip(location_coordinates[0], location_coordinates[1]):
            # Draw invaders
            self._results_padded[y:y + self.invader.height, x:x + self.invader.width] = self.invader.appearance
            # Remove padding
            self.results = self._results_padded[self.pad_value:-self.pad_value, self.pad_value:-self.pad_value]
            # Add normalized coordinates
            self.invader_coordinates.append({"y": y - self.pad_value, "x": x - self.pad_value})

    def get_invader_coordinates(self):
        return self.invader_coordinates
