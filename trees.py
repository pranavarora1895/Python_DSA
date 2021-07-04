class TreeABC:
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element at the given position."""
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        """Return the Position of p's parent"""
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        """Return the number of children that position p has."""
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        """Generate the positions of p's children"""
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        """Return the number of elements in a tree"""
        raise NotImplementedError("must be implemented by subclass")

    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if p is self.root():
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height(self, p):
        """Return the height of the subtree rooted at Position p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))
