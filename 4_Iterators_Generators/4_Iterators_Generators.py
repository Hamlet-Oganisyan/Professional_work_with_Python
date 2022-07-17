from itertools import chain

# Задание 1 Дополнил список до 5 уровня вложенности, работает. 
nested_list = [ ['a', 'b', 'c', [23, 45, 78, ['e', 's', [0, 66, 55], 'k']]], ['d', 'e', 'f'], [1, 2, None] ]

class FlatIterator(list):
    
    def __iter__(self):
        self.element = iter(nested_list)
        return self
        

    def __next__(self):
        next_element = next(self.element)
        if isinstance(next_element, list):
            self.element = chain(next_element, self.element )
            return next(self.element)
        return next_element

for item in FlatIterator(nested_list):
    print(item)     
    
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
         


# # Задание 2
# Обязательное
nested_list_2 = [ ['a', 'b', 'c'], ['d', 'e', 'f'], [1, 2, None] ]

def flat_generator(list):
    # Вариант 1
    for el in  chain.from_iterable(nested_list_2):
        yield el
    # Вариант 2
    # for el in  nested_list_2:
    #     for i in el:
    #         yield i

for item in  flat_generator(nested_list_2):
    print(item)
flat_list_2 = [item for item in flat_generator(nested_list_2)]
print(flat_list_2)


# Дополнительное , список добавлен до 6 уровня вложенности
nested_list_3 = [ ['a', 'b', 'c', [23, 45, 78, ['e', 's', [0, 66, ['q', 'r', 'y'], 55], 'k']]], ['d', 'e', 'f'], [1, 2, None] ]

def flat_generator(nested_list_3):    
    for el in chain(nested_list_3):
        if isinstance(el, list):
            yield from flat_generator(el)
        else:
            yield el
for item in  flat_generator(nested_list_3):
    print(item)
flat_list_3 = [item for item in flat_generator(nested_list_3)]
print(flat_list_3)