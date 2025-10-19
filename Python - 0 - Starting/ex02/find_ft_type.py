def all_thing_is_obj(object: any) -> int:

    obj_type = type(object).__name__
    
    if obj_type == "list":
        print(f"List : {type(object)}")
    elif obj_type == "tuple":
        print(f"Tuple : {type(object)}")
    elif obj_type == "set":
        print(f"Set : {type(object)}")
    elif obj_type == "dict":
        print(f"Dict : {type(object)}")
    elif obj_type == "str":
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    
    return 42

