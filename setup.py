import os
from setuptools import setup, find_packages
import good_practice_examples as app


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


dependency_links = [
    'https://github.com/divio/django-cms/tarball/3a09d5c39b3469e64aeecc0205a193f5b70c2061',  # NOQA
    # needs this dev version for django 1.6 fixes
    'https://github.com/KristianOellegaard/django-hvad/tarball/0e2101f15404eaf9611cd6cf843bfc424117b227',  # NOQA
]


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
        'Django',
        'South',
        'django-libs',
        'Pillow',
        'djangocms_utils',
        'django-countries',
        'django-multilingual-news',
    ],
    dependency_links=dependency_links,
    tests_require=[
        'fabric',
        'factory_boy',
        'django-nose',
        'coverage',
        'django-coverage',
        'mock',
        'flake8',
        'ipdb',
    ],
    test_suite='good_practice_examples.tests.runtests.runtests',
)
