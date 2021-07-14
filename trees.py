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

    def height(self, p=None):

        if p is None:
            p = self.root()
        return self._height(p)


class BinaryTree(TreeABC):
    """Abstract Base class representing Binary Tree Structure"""

    def left(self, p):
        """Return the position of p's left child"""
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """Return the position of p's right child"""
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        """Return Positions of sibling of p. None if root"""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if self.left(parent) == p:
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """Return children of p"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):
    """Linked Representation of Binary Tree Structure"""

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """Returns the element in that Node"""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location"""
            return type(self) is type(other) and self._node is other._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be of proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    # Binary Tree Constructor -----------------------------------------
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        """Returns the position of p's parent"""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Returns the position of left child of p"""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Returns the position of right child of p"""
        node = self._validate(p)
        return self._make_position(self._right)

    def num_children(self, p):
        """Returns the number of children of p"""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        """Place the element at root if tree is empty"""
        if self._root is not None: raise ValueError('Root Exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Create a new left child of parent p"""
        node = self._validate(p)
        if node._left is not None: raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Create a new right child of parent p"""
        node = self._validate(p)
        if node._right is not None: raise ValueError('Left child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        """Replace the element at the given position p by e"""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.
                Return the element that had been stored at Position p.
                Raise ValueError if Position p is invalid or p has two children."""
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p has 2 children')
        child = node._left if node._left is not None else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be a leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('trees must be of same type')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
