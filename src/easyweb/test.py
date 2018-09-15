from jinja2 import Environment, PackageLoader

test_class = {
    "module_name": "mod_name",
    "class_name": "class_name",
    "methods":
        {
            "add": ["a", "b"],
            "subtract": ["a", "b"],
        }

}


def main():
    env = Environment(
        loader=PackageLoader('easyweb', 'templates')
    )

    цшер (env.get_template("template.py").render(data=test_class))
