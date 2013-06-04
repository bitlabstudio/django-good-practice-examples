Django Good Practice Examples
=============================

An app for managing and displaying good practice examples for different
purposes.

Prerequisites
-------------

You will need to have the following packages installed:

* Django
* simple-translation
* Pillow
* South
* django-libs


Installation
------------

If you want to install the latest stable release from PyPi::

    $ pip install django-good-practice-examples

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-good-practice-examples.git#egg=good_practice_examples

Add ``good_practice_examples`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'good_practice_examples',
    )

Run the South migrations::

    ./manage.py migrate good_practice_examples

Hook this app into your ``urls.py``::

    urlpatterns = patterns('',
        ...
        url(r'^goodpractices/', include('good_practice_examples.urls')),
    )

Usage
-----


TODO: Describe usage


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
