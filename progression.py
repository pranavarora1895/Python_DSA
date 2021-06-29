from time import time

start_time = time()
class Progression:
    __slots__ = 'current'

    def __init__(self, start=0):
        self.current = start

    def _advance(self):
        self.current += 1

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            answer = self.current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    __slots__ = 'increment'

    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self.increment = increment

    def _advance(self):
        self.current += self.increment


class GeometricProgression(Progression):
    __slots__ = '_base'

    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self.current *= self._base


class FibonacciProgression(Progression):
    __slots__ = '_prev'

    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self.current = self.current, self._prev + self.current


if __name__ == '__main__':

    print("Default Progression")
    Progression().print_progression(10)
    print("Arithmetic Progression with increment 5")
    ArithmeticProgression(5).print_progression(10)
    print("Arithmetic Progression with increment 5 starts with 2")
    ArithmeticProgression(5, 2).print_progression(10)
    print("Geometric Progression with default base")
    GeometricProgression().print_progression(10)
    print("Geometric Progression with base 3")
    GeometricProgression(3).print_progression(10)
    print("Fibonacci Progression with default start values")
    FibonacciProgression().print_progression(10)
    print("Fibonacci Progression with start values of 4 and 6")
    FibonacciProgression(4, 6).print_progression(10)
    end_time = time()
    elapsed_time = end_time - start_time
    print("Execution time: %0.1f"% elapsed_time)
