from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version'0.1.0',
    author='Mehdi Youssef',
    author_mail='youssef.mehdii@gmail.com',
    description='A utility for backing up PostgreSQL databases. ',
    long_description=log_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MY23/pgbackup',
    packages=find_packages('src')
)
