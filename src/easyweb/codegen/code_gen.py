from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('easyweb', 'templates')  # ,
    #  autoescape=select_autoescape(['html', 'xml'])
)

# template_file = "template.py"
# output_file_name = "flask_application.py"


def create_code(module_name, class_name, methods, template_file, output_file_name):
    template = get_template(template_file)
    template_string = render_template(template, module_name, class_name, methods)
    write(output_file_name, template_string)


def get_template(template_name):
    return env.get_template(template_name)


def render_template(template, module_name, class_name, methods):
    return template.render(module_name=module_name, class_name=class_name, methods=methods)


def write(file_name, template_string):
    with open(file_name, "w") as file:
        file.write(template_string)
