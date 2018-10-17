from setuptools import setup, find_packages

setup(
    name='gme',
    version='1.2',
    description='USITC\'s Gravity Modeling Environment',
    long_description=open('README.txt').read(),
    keywords='gravity estimation ppml',
    url='https://gravity.usitc.gov',
    author='USITC Gravity Modeling Group',
    author_email='gravity@usitc.gov',
    license='LICENSE.txt',
    packages=find_packages(),
    install_requires=['pandas','statsmodels','scipy','patsy'],
    zip_safe=False,
    data_files = [('', ['LICENSE.txt'])]
)
