from distutils.core import setup


setup(
    name='publicsuffix',
    version='0.1',
    description='Fast Python interface to the Public Suffix List',
    author='Brian Cloutier',
    author_email='brian@mixrank.com',
    url='https://github.com/onlinemediagroup/publicsuffix',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    py_modules=['publicsuffix'],
)
