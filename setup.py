from setuptools import setup
import simplerr

setup(name='simplerr',
      version=simplerr.__version__,
      description='The simple request web framework',
      url='https://github.com/yevrah/simplerr',
      author='Javier Woodhouse',
      author_email='javier@wingaru.com.au',
      license='MIT',
      packages=['simplerr'],
      install_requires=[
        'asn1crypto==0.24.0',
        'cffi==1.11.4',
        'click==6.7',
        'colorama==0.3.9',
        'cryptography==2.1.4',
        'idna==2.6',
        'Jinja2==2.10',
        'MarkupSafe==1.0',
        'peewee==3.0.18',
        'pycparser==2.18',
        'pyOpenSSL==17.5.0',
        'redis==2.10.6',
        'six==1.11.0',
        'termcolor==1.1.0',
        'Werkzeug==0.14.1',
        # Doesntwork on windows, but needed for some examples
        # 'mod-wsgi==4.5.24',
      ],
      zip_safe=False)
