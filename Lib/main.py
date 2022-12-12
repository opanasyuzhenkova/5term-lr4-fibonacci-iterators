from fib import *
import test_fib

if __name__ == '__main__':
    print('Fibonacci Seq. <= 20: ', fib(20))


    print(list(range(9)))
    print(list(FibonacchiLst([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))

    fib_iter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    print(list(fib_sequence(10)))

    # test_fib.test_fib_1()
    # test_fib.test_fib_2()