from setuptools import setup

exec(compile(open('test_mark_0001/version.py').read(),
             'test_mark_0001/version.py', 'exec'))

setup(name='test_mark_0001',
      version=__version__,
      description='Test to build a modulule in PyPi',
      keywords='each word in a different seperated by a space not a comma',
      packages=['test_mark_0001'],
      include_package_data=True,
      license='MIT',
      author='Mark Regine, Ph.D.',
      author_email='mregine@betaxanalytics.com',
      url='https://github.com/markregine/test_mark_0001',
      classifiers=['Programming Language :: Python :: 3.5'],
      install_requires=['pandas',
                        'numpy'],
      )
