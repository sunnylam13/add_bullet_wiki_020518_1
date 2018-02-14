try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Add Bullets to Wiki',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/add_bullet_wiki_020518_1',
	'download_url': 'https://github.com/sunnylam13/add_bullet_wiki_020518_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'add_bullet_wiki_020518_1'
}

setup(**config)