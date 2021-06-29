class Vector:
    def __init__(self, d):
        """Create d-dimensional vector of zeros"""
        self._coords = [0] * d

    def __len__(self):
        """Returns the Dimension of Vectors"""
        return len(self._coords)

    def __getitem__(self, i):
        """Return ith coordinate of vector"""
        return self._coords[i]

    def __setitem__(self, i, value):
        """Set ith coordinate to the value """
        self._coords[i] = value

    def __add__(self, other):
        """Return the sum of two vectors"""
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector has different coordinates as other."""
        return not self._coords == other._coords

    def __str__(self):
        """Produce string representation of vector"""
        return '<' + str(self._coords)[1:-1] + '>'

if __name__ == '__main__':
    v1 = Vector(3)
    v2 = Vector(3)
    v1.__setitem__(0,2)
    v1.__setitem__(1,2)
    v1.__setitem__(2,3)
    print(v1)
    v2.__setitem__(0,7)
    v2.__setitem__(1,3)
    v2.__setitem__(2,5)
    print(v2)
    print(v1.__add__(v2))
    print(v1.__eq__(v2))
    print(v1.__ne__(v2))

help(Vector)