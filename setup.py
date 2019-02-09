from setuptools import setup

#exec(compile(open('zepid/version.py').read(),
#             'zepid/version.py', 'exec'))

setup(name='Test_mark_0001',
      version=__version__,
      description='Test to build a modulule in PyPi',
      keywords='each word in a different seperated by a space not a comma',
      packages=['Test_mark_001'],
      include_package_data=True,
      license='MIT',
      author='Mark Regine, Ph.D.',
      author_email='mregine@betaxanalytics.com',
      url='https://github.com/markregine/Test_mark_0001',
      classifiers=['Programming Language :: Python :: 3.5'],
      install_requires=['pandas>=0.18',
                        'numpy'],
      )
