#!/usr/bin/env python3

from typing import List, Tuple
from pathlib import Path


class SpotItDeck:
    """
    Class to create and work with a "SpotIt!" deck. The generation is based on a projective plane
    PG(2, n) with n²+n+1 points and lines. n+1 points are on each line, n+1 lines on each point.
    Default value for the normal SpotIt deck is 7, leading to 57 cards.
    """

    def __init__(self, images_dir: Path, n: int = 7):
        self.point_sets = self._generate_projective_plane_lines(n)
        i = 0
        for point_set in self.point_sets:
            i += 1
            card_image_numbers = [x * n + y for x, y in point_set]
            print(f"Card {i}: {card_image_numbers}")
        # image_paths = [images_dir.iterdir()]  # todo: filter non-image files
        # points = [(x, y) for x in range(n) for y in range(n)]
        # self.points_to_images_map = {
        #     point: image_path for point, image_path in zip(points, image_paths)
        # }

    def _generate_projective_plane_lines(self, n) -> List[Tuple[int, int]]:
        infinity_point = (n, n)
        infinity_points_line = [(n, m) for m in range(n)] + [infinity_point]

        lines = [
            SpotItDeck.generate_non_vertical_line(m, b, n)
            for m in range(n)
            for b in range(n)
        ] + [SpotItDeck.generate_vertical_line(x, n) for x in range(n)]
        lines += [infinity_points_line]

        return lines

    @staticmethod
    def generate_non_vertical_line(m, b, n):
        return [(x, (m * x + b) % n) for x in range(n)] + [(n, m)]

    @staticmethod
    def generate_vertical_line(x, n) -> List[Tuple[int, int]]:
        infinity_point = (n, n)
        return [(x, y) for y in range(n)] + [infinity_point]


if __name__ == "__main__":
    deck = SpotItDeck(Path("images"))
