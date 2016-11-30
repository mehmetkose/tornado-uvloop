
from distutils.core import setup

setup(
    name='tornado-uvloop',
    version='0.1.2',
    packages=['tornadouvloop'],
    url='https://github.com/mehmetkose/tornado-uvloop',
    license='WTFPL',
    author='Mehmet Kose',
    author_email='mehmet@linux.com',
    description='super simple uvloop class for tornado framework',
    platforms=('linux'),
    keywords=['tornado','asyncio','uvloop'],
    install_requires=[
        'tornado>=4.4.2',
        'rethinkdb>=3.2.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Utilities",
    ],
)
