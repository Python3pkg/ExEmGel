from setuptools import setup

with open('README.txt') as file:
    long_description = file.read()

setup(
    name='TowelStuff',
    version='0.1.dev1',
    packages=['towelstuff',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python :: 3.3',
    ],
)
