def NULL_not_found(object: any) -> int:
    type_object = type(object)
    # print(f"Type: {type_object}, obj ={object}")
    if (object == None):
        print(f"Nothing: None {type_object}")
    elif (isinstance(object, float) and object != object):
        print(f"Cheese :nan {type_object}")
    elif (isinstance(object, bool) and object == False):
        print(f"Fake: False {type_object}")
    elif (isinstance(object, int) and object == 0):
        print(f"Zero : 0 {type_object}")
    elif (isinstance(object, str) and object == ""):
        print(f"Empty : {type_object}")
    else:
        print("Type not Found")
        return (1)
    return (0)
