from setuptools import setup

setup(name='ParadiseBlackbox',
      version='0.1',
      description='A python package for easily interacting with Paradise SS13 Blackbox data and caching it locally',
      url='http://github.com/storborg/funniest',
      author='Ryan Longo',
      license='MIT',
      packages=['paradise_blackbox'],
      install_requires=[
          'requests',
          'matplotlib',
          'numpy',
      ],
      zip_safe=False)
