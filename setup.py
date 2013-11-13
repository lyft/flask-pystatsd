"""
Flask-pystatsd
-------------

Flask-pystatsd is an extension which makes it easy for Lyft developers to send metrics to statsd.
"""
from setuptools import setup


setup(
    name='Flask-pystatsd',
    version='0.1',
    url='https://github.com/lyft/flask-pystatsd',
    license='BSD',
    author='Elijah Chancey',
    author_email='elijah.chancey@lyft.com',
    description='Does away with boilerplate code for sending metrics to statsd.',
    long_description=__doc__,
    packages=['flask_pystatsd'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
