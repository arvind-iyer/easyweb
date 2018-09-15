from flask import Flask, jsonify
app = Flask(__name__)

import {{ data[module_name] }}
{{ data[class_name] }}_instance = {{ data[module_name] }}.{{ data[class_name] }}()

{% for method_name in data[methods] %}

@app.route("/{{ method_name }}")
def {{ method_name }}():
	result = {{ data[class_name] }}_instance.{{ method_name }}( ', '.join(data[methods][method_name] ))
	return jsonify(result)

{% endfor %}