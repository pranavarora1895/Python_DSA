class SequenceIterator:
    """An Iterator for any Python's Sequence Types"""
    def __init__(self, sequence):
        """Create an Iterator for Sequence Types"""
        self._seq = sequence
        self._k = -1

    def __next__(self):
        """Return the next element, or Raise StopIteration Error"""
        self._k+=1
        if self._k<len(self._seq):
            return (self._seq[self._k])
        else:
            raise StopIteration()

    def __iter__(self):
        """By convention, iterator must return itself as an iterator"""
        return self

if __name__ == '__main__':
    seq = SequenceIterator([4,3,5])
    print(list(seq.__iter__()))
