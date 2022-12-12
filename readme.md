### Лабораторная работа 4. Ряд Фибоначчи с помощью итераторов

#### Задание 1

Разработать функцию, возвращающую элементы ряда Фибоначчи 
по данному максимальному значению.

Требуется реализовать код для функции `fib` такой что, 
для данного `n` функция возвращала бы максимальное число 
элементов ряда Фибоначчи не превосходящих данное `n`.

Например: для n = 1, функция должна вернуть 
список `[0, 1, 1]`. Для n = 2, соответственно 
`[0, 1, 1, 2]`. Для n = 5, соответственно `[0, 1, 1, 2, 3, 5]`.

```python
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
```

#### Задание 2

Дополните код классом FibonacchiLst, который бы позволял 
перебирать элементы из ряда Фибоначчи по данному ей списку. 
Итератор должен вернуть очередное значение, которое 
принадлежит ряду Фибоначчи, из данного ей списка. 
Например: для `lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, 
FibonacchiLst должен вернуть `[0, 1, 1, 3, 5, 8]`

Решение может быть выполнено с помощью реализации 
содержимого методов `__init__`,`__iter__`, `__next__` или 
с помощью реализации метода `__getitem__`.

```python
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
```
#### Задание 3

Для выполнения задания требуется написать такую функцию 
`fib_iter`, которая принимала бы iterable-объект 
с числами и возвращала бы числовые значения 
(принадлежащие ряду Фибоначчи) с помощью модуля 
`itertools` (например, с помощью метода `islice()`):

```python
def fib_iter(iterable_object):
    '''Function takes an iterable object as input and returns elems of Fibonacci Seq
    '''
    n = len(iterable_object)
    li = []
    fr = filter(lambda x: x in fib(n), iterable_object)
    print(list(fr))
```

#### Задание 4
Создание программы с классическим генератором 
(использовать yield).

```python
def fib_sequence(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
```