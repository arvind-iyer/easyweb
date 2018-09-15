from easyweb.codegen.code_gen import create_code
import os.path


def test_template_reading():
    module_name = "my_easy_web_test"
    class_name = "ClassExample"
    methods = {
        "my_method": ["a", "b"]
    }
    create_code(module_name, class_name, methods, "../template.py", "output.py")
    assert(os.path.isfile("output.py"))
