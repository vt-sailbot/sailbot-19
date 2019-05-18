import math
import numpy as np


class Vec(object):
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        if isinstance(other, Vec):
            return Vec(self.data + other.data)
        return Vec(self.data + other)

    def __radd__(self, other):
        return Vec(other + self.data)

    def __sub__(self, other):
        if isinstance(other, Vec):
            return Vec(self.data - other.data)
        return Vec(self.data - other)

    def __rsub__(self, other):
        return Vec(other - self.data)

    def __mul__(self, other):
        if isinstance(other, Vec):
            return Vec(self.data * other.data)
        return Vec(self.data * other)

    def __rmul__(self, other):
        return Vec(other * self.data)

    def __div__(self, other):
        if isinstance(other, Vec):
            return Vec(self.data / other.data)
        return Vec(self.data / other)

    def __rdiv__(self, other):
        return Vec(other / self.data)

    def __neg__(self):
        return Vec(-self.data)

    def __pos__(self):
        return Vec(+self.data)

    def __eq__(self, other):
        return np.array_equal(self.data, other.data)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.square_length() < other.square_length()

    def __le__(self, other):
        return self.square_length() <= other.square_length()

    def __gt__(self, other):
        return self.square_length() > other.square_length()

    def __ge__(self, other):
        return self.square_length() >= other.square_length()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return np.array_str(self.data)

    def ceil(self):
        return Vec(np.ceil(self.data))

    def floor(self):
        return Vec(np.floor(self.data))

    def get_data(self):
        return self.data

    def inverse(self):
        return Vec(1.0/self.data)

    def length(self):
        return float(np.linalg.norm(self.data))

    def normalize(self):
        length = self.length()
        if length == 0.0:
            return Vec(np.zeros(self.data.shape()))
        return Vec(self.data/length)

    def round(self, decimal=0):
        return Vec(np.round(self.data, decimal))

    def square_length(self):
        return float(np.sum(np.square(self.data)))

    @classmethod
    def distance(cls, a, b):
        c = b - a
        return c.length()

    @classmethod
    def dot(self, a, b):
        return Vec(np.dot(a.data, b.data))

    @classmethod
    def equals(cls, a, b, tolerance=0.0):
        diffs = np.fabs((a - b).data)
        pairs = zip(list(np.fabs(a.data)), list(np.fabs(b.data)))
        tolerance_calcs = [tolerance * max(1, a_val, b_val) for (a_val, b_val) in pairs]
        tests = [d <= t for (d, t) in zip(diffs, tolerance_calcs)]
        return all(tests)

    @classmethod
    def max_components(cls, a, b):
        return Vec(np.maximum(a.data, b.data))

    @classmethod
    def min_components(cls, a, b):
        return Vec(np.minimum(a.data, b.data))

    @classmethod
    def mix(cls, a, b, t):
        return a*(1-t) + b*t

    @classmethod
    def random(cls, n):
        return Vec(np.random.rand(n))

    @classmethod
    def square_distance(cls, a, b):
        c = b - a
        return c.square_length()


class Vec2(Vec):
    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)
        super(Vec2, self).__init__(np.array([x, y], dtype=np.float32))

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = float(new_x)
        self.data[0] = self._x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = float(new_y)
        self.data[1] = self._y

    def angle(self):
        return math.atan(self.y / self.x)

