import inspect

def classmethods(class_object):
    """Takes an object and returns a list of names of all the methods
    in that class
    :param class_object : instance of any Class in python
    :return : list of method names as strings
    """
    fn_tuple_list = inspect.getmembers(class_object, predicate=inspect.ismethod)
    fn_names = [f_name for (f_name, method) in fn_tuple_list
                        if not f_name.startswith('_')]
    return fn_names
