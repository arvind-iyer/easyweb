import inspect


def classmethods(class_object):
    """Takes an object and returns a list of names of all the methods
    in that class
    :param class_object : instance of any class in python
    :return : list of method names as strings
    """
    fn_tuple_list = inspect.getmembers(class_object, predicate=inspect.ismethod)
    fn_names = [
        f_name for (f_name, method) in fn_tuple_list if not f_name.startswith("_")
    ]
    return fn_names


def argnames(method):
    """Takes a function as parameter and returns a list of argument names
    :param method: function to inspect
    :return : list of argument names except the 'self' object
    """
    return [arg for arg in method.__code__.co_varnames if arg != "self"]


def create_methods_dict(class_object):
    """
    """
    fn_tuple_list = inspect.getmembers(class_object, predicate=inspect.ismethod)
    methods = dict()
    for (f_name, method) in fn_tuple_list:
        if f_name.startswith("_"):
            continue
        methods[f_name] = argnames(method)

    return methods


def classname(class_object):
    """Returns name of class of an instance as a str
    :param class_object : Instance of any class
    :return : name of class as string
    """
    return class_object.__class__.__name__


def modulename(class_object):
    return class_object.__class__.__module__


def main(class_object):
    return {
        "module_name": modulename(class_object),
        "class_name": classname(class_object),
        "methods": create_methods_dict(class_object),
        "object": class_object,
    }
