from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='should-plone',
      version=version,
      description="Should DSL matchers for Plone",
      long_description="""\
Should DSL matchers for Plone CMS""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Rogerio Atem de Carvalho',
      author_email='ratembd@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'should_dsl'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

