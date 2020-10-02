from setuptools import setup, find_packages

with open('README.md') as f:
    readme_text = f.read()

setup(
    name='marketertech',
    version='0.0.1',
    description='Exercise for Marketer Techonolgies',
    long_description=readme_text,
    author='Filip Geppert',
    author_email='filip.geppert@gmail.com',
    url='',
    packages=find_packages(exclude=('tests',))
)
