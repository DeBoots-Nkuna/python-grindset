"""
    This file contains calculator operations functionalties
    +,*,- and /. 
    the operations will be stored in the dictionary as keys and
    each method as value to its correct key
"""

#function definitions

def add(n1, n2):
    return n1+ n2

def multiply(n1,n2):
    return n1 * n2

def subtract(n1,n2):
    return n1 - n2

def divid(n1, n2):
    return n1/ n2


#dictionary to store operations and their corresponding methods

operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divid
}    



