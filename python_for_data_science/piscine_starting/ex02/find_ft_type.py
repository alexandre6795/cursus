def all_thing_is_obj(object: any) -> int:
    if (object):
        type_object = type(object)
        typename = type_object.__name__
        typename = typename[0] + typename[1:]
        if (type_object == str):
            print(f"{object} is in the kitchen : {type_object}")
        else:
            print(f"{typename} : {type_object}")
        return (42)
