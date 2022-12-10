import itertools

def fib(n):
    """
    The function returns elements of the Fibonacci series not exceeding n

    Keyword arguments:
    n - the number up to which the Fibonacci sequence should be output
    """
    fib1 = 0
    fib2 = 1
    li = [fib1, fib2]
    i = 1
    while fib1 + fib2 <= n:
        if n == 1:
            return li
        else:
            fib1, fib2 = fib2, fib1 + fib2
            li.append(fib2)
            i += 1
    return li


class FibonacchiLst():
    def __init__(self, instance):
        self.instance = instance
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                res = self.instance[self.idx]
            except IndexError:
                raise StopIteration
            if res == 1:
                self.idx += 1
                return res, res
            if res in fib(len(self.instance)):
                self.idx += 1
                return res
            else:
                self.idx += 1


def fib_iter(iterable_object):
    '''Function takes an iterable object as input and returns elems of Fibonacci Seq
    '''
    n = len(iterable_object)
    li = []
    fr = filter(lambda x: x in fib(n), iterable_object)
    print(list(fr))

def fib_sequence(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b






