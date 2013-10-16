from setuptools import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='ExEmGel',
    version='0.1',
    packages=['exemgel',],
    license='MIT',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 2.6',
    ],
)
