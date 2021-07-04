# -*- coding: utf-8 -*-
import base64
import functools
import os
import pathlib
import shutil

from jinja2 import Environment, FileSystemLoader, select_autoescape
from jinja2.exceptions import TemplateNotFound

import settings


def get_template_names(info):
	"""
	Generates template names with specific template order. For template 404:

	404.html
	40x.html
	4xx.html
	error.html
	"""
	return [
		f'{info["value"]}.html',
		f'{info["value"][:2]}x.html',
		f'{info["value"][:1]}xx.html',
		f'error.html',
	]


def get_context(info):
	info = info.copy()
	info['code'] = info['value']
	details = info.get('details')
	if details:
		info['details'] = details[0].get('description')
	return info


def b64_read(directory, filename):
	with open(directory / filename, 'rb') as fp:
		return base64.b64encode(fp.read()).decode('ascii')


def generate(directory):
	os.makedirs(directory / 'output', exist_ok=True)
	env = Environment(
		loader=FileSystemLoader(directory / 'templates'),
		autoescape=select_autoescape()
	)
	env.globals['b64_read'] = functools.partial(b64_read, directory)
	for info in settings.HTTP_CODES:
		ctx = get_context(info)
		templates = get_template_names(info)
		template = None
		for template_name in templates:
			try:
				template = env.get_template(template_name)
			except TemplateNotFound:
				continue
			else:
				break

		if template is None:
			continue

		rendered = template.render(**ctx)
		with open(directory / 'output' / (info['value'] + '.html'), 'w') as fp:
			fp.write(rendered)

	try:
		shutil.copytree(directory / 'static', directory / 'output', dirs_exist_ok=True)
	except OSError:
		pass


def main():
	script_dir = pathlib.Path(__file__).resolve().parent
	generate(script_dir)


if __name__ == "__main__":
	main()
