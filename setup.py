from setuptools import setup, find_packages

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='drf_useful_decorators',
      version='0.0.5',
      description='Useful decorators for working with Django Rest Framework.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      keywords='django rest drf atomic exception endpoints',
      url='https://github.com/Zadrote5/drf-useful-decorators',
      author='Zadrote5',
      author_email='braynt.k@mail.ru',
      license='Apache License, Version 2.0, see LICENSE file',
      packages=find_packages(),
      install_requires=[
          'djangorestframework',
          'django'
      ],
      include_package_data=True,
      zip_safe=False)