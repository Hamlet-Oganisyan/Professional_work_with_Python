my_list = [ ['a', 'b', 'c'], ['d', 'e', 'f'], [1, 2, None] ]

def flat_generator(my_list ):    
   for el in  chain.from_iterable(my_list ):
        yield el
        flat_list = [item for item in flat_generator(my_list )]
        print(flat_list)