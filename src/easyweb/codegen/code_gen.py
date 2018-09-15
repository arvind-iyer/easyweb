from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('easyweb', 'templates')  # ,
    #  autoescape=select_autoescape(['html', 'xml'])
)

# template_file = "template.py"
# output_file_name = "flask_application.py"


def create_code(data, template_file, output_file_name):
    template = get_template(template_file)
    template_string = render_template(template, data)
    write(output_file_name, template_string)


def get_template(template_name):
    return env.get_template(template_name)


def render_template(template, data):
    return template.render(data)


def write(file_name, template_string):
    with open(file_name, "w") as file:
        file.write(template_string)
