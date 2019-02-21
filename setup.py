from setuptools import setup
from botapitit import version


def long_description():
    with open("README.md") as f:
        ld = f.read()
    return ld


setup(name='botapitit',
      version=version.__version__,
      description='Universal API for building bots',
      long_description=long_description(),
      long_description_content_type='text/markdown',
      url='https://github.com/Lgmrszd/bot_apitit',
      author='Lgmrszd',
      author_email='m.v.bobrov@yandex.ru',
      license='GPL-3.0-or-later',
      packages=['botapitit'],
      classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ])
