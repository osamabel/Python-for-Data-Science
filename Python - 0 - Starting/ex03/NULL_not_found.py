import math

def NULL_not_found(object: any) -> int:
    #your code here
    obj_type = type(object).__name__
    
    if object is None:
        print(f"Nothing: {object} <class 'NoneType'>")
        return 0
    elif isinstance(object, float) and math.isnan(object):
        print(f"Cheese: {object} <class 'float'>")
        return 0
    elif isinstance(object, bool) and object == False:
        print(f"Fake: {object} <class 'bool'>")
        return 0
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} <class 'int'>")
        return 0
    elif isinstance(object, str) and object == "":
        print(f"Empty: <class 'str'>")
        return 0
    else:
        print("Type not Found")
        return 1

