# dataclasses are mutable by default
# dataclasses and namedtuple have better repr()

from collections import namedtuple
from typing import NamedTuple

Coordinate = namedtuple('Coordinate', 'lat lon')
# named tuple is a subclass of tuple

Coordinate = NamedTuple('Coordinate', [('lat', float), ('lon', float)])


# this will also be sublcass of tuple only
class Coordinate(NamedTuple):
    lat: float
    lon: float