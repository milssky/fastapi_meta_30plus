from typing import Type, TypeVar


class Geometry: ...


T = TypeVar('T', bound=Geometry)
K = TypeVar('K')
V = TypeVar('V', int, float)  # V[int], V[float]. V[...] 


class Point2D(Geometry): ...


def factory_point(cls_geom: Type[T]) -> T:
    return cls_geom()


geometry_obj: Geometry = factory_point(Geometry)  # T = Geometry
point: Point2D = factory_point(Point2D)  # T = Point2D

print(type(geometry_obj))
print(type(point))


class Myclass(metaclass=...):...