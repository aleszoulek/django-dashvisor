import os
from setuptools import setup


try:
    f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
    long_description = f.read().strip()
    f.close()
except IOError:
    long_description = None

setup(
    name='django-dashvisor',
    version='0.1',
    url="http://github.com/aleszoulek/django-dashvisor",
    description='Supervisor dashboard',
    long_description=long_description,
    author='Ales Zoulek',
    author_email='ales.zoulek@gmail.com',
    license='BSD',
    keywords='supervisor dashboard remote control'.split(),
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    include_package_data=True,
)

