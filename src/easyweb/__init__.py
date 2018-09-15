from . import core as ec
from .codegen.code_gen import create_code


def run(obj, template_file="template.py", output_file="app.py"):
    create_code(ec.main(obj), template_file, output_file)
