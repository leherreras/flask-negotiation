"""
Flask-Negotiation
==================

Provides better content negotiation for flask.
"""
from setuptools import setup, find_packages
from codecs import open
from os import path


with open(path.join(path.abspath(path.dirname(__file__)), 'requirements.txt')) as f:
    requirements = [item for item in f.read().split('\n') if item]

setup(
      name='Flask-Negotiation',
      version='1.0.0',
      description='Better content negotiation for flask',
      url='https://git.cytac.org/mat/flask-negociation.git',
      author='Luis Carlos Herrera (CTAS-MAT)',
      author_email='luis.herrera@cyxtera.com',
      packages=find_packages(exclude=["tests.*", "tests"]),
      install_requires=requirements,
      zip_safe=False
)
