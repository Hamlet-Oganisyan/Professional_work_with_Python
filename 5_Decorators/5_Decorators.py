from datetime import datetime
import functools
from itertools import chain

# Задание 1
def multiplication(a, b):
    return a*b

def logger(old_function):
    def foo(a, b):
        date_time = datetime.now()
        result = old_function(a, b)
        log_data = f'Дата и время вызова функции: {date_time}\nИмя вызываемой функции: {old_function.__name__}\nАргументы функции {a}, {b}\nФункция {old_function.__name__} вернула {result}'
        # print(log_data)
        with open('logs/first.log', 'a') as file:
            file.write(log_data)
        return result
    return foo
mult = logger(multiplication)
mult(9, 5)


# Задание 2
def param_logger(path):
    def _param_logger(some_function):
        # @wraps(some_function)
        def foo(*args, **kwargs):
            date_time = datetime.now()
            result = some_function(*args, **kwargs)
            # a, b = args, kwargs
            log_data = f'Дата и время вызова функции: {date_time}\nИмя вызываемой функции: {some_function.__name__}\nАргументы функции {*args, *kwargs}\nФункция {some_function.__name__} вернула {result}\n'
            with open(path, 'a') as file:
                file.write(log_data)
            return result
        return foo
    return _param_logger

@param_logger('logs/second.log')
def multiplication(a, b):
    return a*b

result = multiplication(6, 7)


# Задание 3 Применить написанный логгер к приложению из любого предыдущего д/з.
my_list = [ ['a', 'b', 'c'], ['d', 'e', 'f'], [1, 2, None] ]

@param_logger('logs/third.log')
def flat_generator(list):    
    for el in  list:
        for i in el:
            yield i

result = [item for item in flat_generator(my_list)]
print(result)