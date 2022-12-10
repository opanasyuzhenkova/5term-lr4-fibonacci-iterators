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


#### Задание 3

Для выполнения задания требуется написать такую функцию 
`fib_iter`, которая принимала бы iterable-объект 
с числами и возвращала бы числовые значения 
(принадлежащие ряду Фибоначчи) с помощью модуля 
`itertools` (например, с помощью метода `islice()`):


#### Задание 4
Создание программы с классическим генератором 
(использовать yield).