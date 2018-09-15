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


def classname(class_object):
    """Returns name of class of an instance as a str
    :param class_object : Instance of any class
    :return : name of class as string
    """
    return class_object.__class__.__name__
