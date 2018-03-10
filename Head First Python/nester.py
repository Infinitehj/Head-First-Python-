"""
这是nester.py模块，提供了一个名为print_lol()函数,作用为打印列表，其中可能包含（也可能不包含）嵌套列表。
This is the "nester.py" module and it provides one function called print_lot() which prints lists that may or may not nested lists.
"""
#version = 1.0.0
def print_lol(the_list):
    """
    This function takes one positional argument called "the list",which is any Python list (of - possibly - nested lists). Each data item in the provided list is (recursively) printed to the screen on it's own line.
    """
    for each_item in the_list:      
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)


#version = 1.1.0
def print_lol1(the_list,level=0):

    for each_item in the_list:      
        if isinstance(each_item,list):
            print_lol1(each_item,level+1)
        else:
            for tab in range(level):
                print('\t', end='')
            print(each_item)

#version = 1.2.0
def print_lol2(the_list,indent = False, level=0):

    for each_item in the_list:      
        if isinstance(each_item,list):
            print_lol2(each_item,indent,level+1)
        else:
            if indent:
                for tab in range(level):
                    print('\t', end='')
                print(each_item)
                
movies = ['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91,
              ['Graham Chapman', 
                  ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]
print_lol(movies)
print_lol1(movies)
print_lol2(movies,True,1)