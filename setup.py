
from distutils.core import setup

setup(
    name='tornado-uvloop',
    version='0.2.0',
    packages=['tornadouvloop'],
    url='https://github.com/mehmetkose/tornado-uvloop',
    license='MIT',
    author='Mehmet Kose',
    author_email='mehmetkose122@gmail.com',
    description='super simple uvloop class for tornado framework',
    platforms=('linux'),
    keywords=['tornado','asyncio','uvloop'],
    install_requires=[
        'tornado>=4.4.0',
        'uvloop>=0.6.0',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Environment :: Web Environment",
        "Topic :: Utilities",
    ],
)
