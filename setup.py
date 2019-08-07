from distutils.core import setup

packages = ['toolzEx']
install_requires = ['toolz>=0.10.0']

setup(name='toolzEx',
      version='0.1',
      author='Felix G. Knorr',
      author_email='knorr.felix@gmx.de',
      url='https://github.com/KnorrFG/toolzEx',
      packages=packages,
      install_requires=install_requires,
      python_requires='>=3.7')
