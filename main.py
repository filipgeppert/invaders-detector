from source.entities import Invader, Radar, RadarSample
from source.utilities import Serializer
from typing import List

import argparse


def main(invaders_contours: List[str], radar_sample_str: str, precision: float):
    """
    Detects invaders for a given radar sample.
    Prints results and invader coordinates.
    """
    # Run analysis
    invaders = [Invader(Serializer.sample_to_array(i)) for i in invaders_contours]
    radar_sample = RadarSample(Serializer.sample_to_array(radar_sample_str))
    radar_readings = [Radar(invader=invader, radar_sample=radar_sample, precision=precision)
                      for invader in invaders]

    # Locate invaders and print results
    for radar_reading in radar_readings:
        radar_reading.locate_invader()
        print(f"Coordinates: {radar_reading.get_invader_coordinates()}")
        print(Serializer.array_to_sample(radar_reading.results))


if __name__ == '__main__':
    known_invaders_contours = [
        """--o-----o--
            ---o---o---
            --ooooooo--
            -oo-ooo-oo-
            ooooooooooo
            o-ooooooo-o
            o-o-----o-o
            ---oo-oo---""",
        """---oo---
            --oooo--
            -oooooo-
            oo-oo-oo
            oooooooo
            --o--o--
            -o-oo-o-
            o-o--o-o"""
    ]
    known_radar_sample = """----o--oo----o--ooo--ooo--o------o---oo-o----oo---o--o---------o----o------o-------------o--o--o--o-
                        --o-o-----oooooooo-oooooo---o---o----o------ooo-o---o--o----o------o--o---ooo-----o--oo-o------o----
                        --o--------oo-ooo-oo-oo-oo-----O------------ooooo-----oo----o------o---o--o--o-o-o------o----o-o-o--
                        -------o--oooooo--o-oo-o--o-o-----oo--o-o-oo--o-oo-oo-o--------o-----o------o-ooooo---o--o--o-------
                        ------o---o-ooo-ooo----o-----oo-------o---oo-ooooo-o------o----o--------o-oo--ooo-oo-------------o-o
                        -o--o-----o-o---o-ooooo-o-------oo---o---------o-----o-oo-----------oo----ooooooo-ooo-oo------------
                        o-------------ooooo-o--o--o--o-------o--o-oo-oo-o-o-o----oo------------o--oooo--ooo-o----o-----o--o-
                        --o-------------------------oo---------oo-o-o--ooo----oo----o--o--o----o--o-o-----o-o------o-o------
                        -------------------o----------o------o--o------o--------o--------o--oo-o-----oo-oo---o--o---o-----oo
                        ----------o----------o---o--------------o--o----o--o-o------------oo------o--o-o---o-----o----------
                        ------o----o-o---o-----o-o---o-----oo-o--------o---------------------------------o-o-o--o-----------
                        ---------------o-------o-----o-------o-------------------o-----o---------o-o-------------o-------oo-
                        -o--o-------------o-o-----o--o--o--oo-------------o----ooo----o-------------o----------oo----o---o-o
                        -o--o-------------o----oo------o--o-------o--o-----o-----o----o-----o--o----o--oo-----------o-------
                        -o-----oo-------o------o----o----------o--o----o-----o-----o-------o-----------o---o-o--oooooo-----o
                        -o--------o-----o-----o---------oo----oo---o-o---------o---o--oooo-oo--o-------o------oo--oo--o-----
                        ------------o---------o---------o----oooo-------------oo-oo-----ooo-oo-----o-------o-oo-oooooooo---o
                        ----------------------o------------oooooooo---o-----o-------o--oooooo-o------------o-o-ooooooo-o----
                        ------------o------o---o---o-------oo-oo--o--o---------o--o-o-o-ooooo-o--------------oo-o----o-oo-o-
                        ---o-o----------oo-------oo----o----oooooooo-------o----o-o-o-o-----o-o-----o----------ooo-oo--o---o
                        -o-o---------o-o---------------o--o--o--ooo---ooo-------o------oo-oo------------o--------o--o-o--o--
                        -------oo---------------------------o-oo----------o------o-o-------o-----o----o-----o-oo-o-----o---o
                        ---o--------o-----o-------o-oo-----oo--oo-o----oo----------o--o---oo------oo----o-----o-------o-----
                        ---o--ooo-o---------o-o----o------------o---------o----o--o-------o----o--------o----------------oo-
                        ---o------o----------------o----o------o------o---oo-----------o-------------o----------oo---------o
                        --oo---------------o--o------o---o-----o--o-------------o------o-------o-----o-----o----o------o--o-
                        -o-------o----------o-o-o-------o-----o--o-o-----------o-oo-----------o------o---------o-----o-o----
                        ----------o----o-------o----o--o------o------------o---o---------------oo----o-----ooo--------------
                        ----o--------oo----o-o----o--o------ooo----o-oooo---o--o-oo--------o-oo-----o-o---o-o--o-----oo-----
                        ------o--------o-ooooo----o---o--o-----o---------------o-o-------o-----o----------------------------
                        o-------oo----o--oooooo-o---o--o------oooo----------o-oo-------o---o----------o------oo-------------
                        -o---o----------o--oo-oo-o---o-----o-o-----------------------oo--o------o------o--------------------
                        -----oo-o-o-o---ooooooooo----o----o--------o--o---oo---o------------o----------o-o---o------o-o--oo-
                        ------o------o---ooo-o---------------------------o--o---o---o----o--o-------o-----o------o----o----o
                        -------o----------ooo-o-----o----o---o--o-oo--o--o-o--o------o--o-oo---ooo------------------------o-
                        -o-------o------o-o--ooo--o---o---oo-----o----o-------------o----o-ooo-o------o--o-o------o-o-------
                        ---oo--o---o-o---------o---o--------------o--o-----o-------o-----o--o---o-oo--------o----o----o-----
                        o------o----oo-o-----------oo--o---o--------o-o------o-------o-o------o-oo---------o-----oo---------
                        ----o--o---o-o-----------o---o------------o-------o----o--o--o--o-o---------------o-----------------
                        -------oo--o-o-----o-----o----o-o--o----------------------o-------o------o----oo----ooo---------o---
                        o-----oo-------------------o--o-----o-----------o------o-------o----o-----------o----------------o--
                        --o---o-------o------------o--------------------o----o--o-------------oo---o---------oo--------o----
                        --o--------o---------o------------o------o-------o------------o-------o---o---------ooooo-----------
                        ------o--------------o-o-o---------o---o-------o--o-----o-------o-o----------o-----oo-ooo----------o
                        --o---------------o----o--oo-------------o---------o-------------------oo---------oo-o-ooo----------
                        -o-----------o------ooo----o----------------ooo-----o--------o--o---o-----------o-o-oooooo--------oo
                        -o---o-------o---o-oooo-----o-------------------o----oo-----------------o--o--------o--o------o--o--
                        -------o---o------oooooo--o----ooo--o--------o-------o----------------------------oo-oo-o--o--------
                        o--oo------o-----oo--o-oo------------oo--o------o--o-------------oo----o------------oooo-o------oo--
                        -----o----------ooooooooo--------------oo--------------oo-----o-----o-o--o------o----------o----o---"""

    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", help="float value between 0 and 1",
                        type=float, default=0.75)
    args = parser.parse_args()

    main(invaders_contours=known_invaders_contours, radar_sample_str=known_radar_sample, precision=args.precision)
