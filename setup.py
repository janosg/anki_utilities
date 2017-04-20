from setuptools import setup, find_packages

pkg = find_packages()
print('\n\n\nthis is the package list:\n', pkg, '\n\n')

setup(
    name='anki_utilities',
    version='0.0.007',
    packages=pkg
)
