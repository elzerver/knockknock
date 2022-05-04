from setuptools import setup, find_packages

requires = [
    'flask',
    'requests',
    'requests_html',
    'pathlib'
]

setup(
    name='knockknock',
    version='1.0',
    description='A login page using openid authentication or similar',
    author='me',
    author_email='',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)