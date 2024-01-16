#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as reqs:
    requirements = reqs.read()

test_requirements = [ ]

setup(
    author="Georgi Karadzhov",
    author_email='georgi.m.karadjov@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A toolkit for evaluating deliberative discussions and building DEliBots. For more details see delibot.xyz",
    install_requires=["sentence-transformers>=2.2.2", "torch>=2.1.2", "transformers>=4.20.1", "numpy>=1.24.4",
                      "scikit-learn==1.2.2"],
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='delitoolkit',
    name='delitoolkit',
    packages=find_packages(include=['delitoolkit', 'delitoolkit.*']),
    package_data={'delitoolkit': ['models', 'delidata_corpus']},
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/gkaradzhov/delitoolkit',
    version='0.3.9',
    zip_safe=False,
)
