import os
from setuptools import setup, find_packages
import good_practice_examples as app


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="django-good-practice-examples",
    version=app.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, good, practice, examples, list, display',
    author='Daniel Kaufhold',
    author_email='daniel.kaufhold@bitmazk.com',
    url="https://github.com/bitmazk/django-good-practice-examples",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.4.3',
        'South',
        'django-libs',
        'simple-translation',
        'Pillow',
        'django-cms',
        'djangocms_utils',
        'django-countries',
        'django-multilingual-news',
    ],
    tests_require=[
        'fabric',
        'factory_boy<2.0.0',
        'django-nose',
        'coverage',
        'django-coverage',
        'mock',
        'flake8',
        'ipdb',
    ],
    test_suite='good_practice_examples.tests.runtests.runtests',
)
