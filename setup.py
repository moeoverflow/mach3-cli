"""
Recursively parse, index and query subtitle text.
"""
from setuptools import find_packages, setup

setup(
    name='mach3',
    version='0.1.1.0.4',
    url='https://github.com/Calvin-Xu/mach3-cli',
    download_url = 'https://github.com/Calvin-Xu/mach3-cli/archive/0.1.tar.gz',
    license='MIT',
    author='Pinlin Xu',
    author_email='calvinxu806@gmail.com',
    description='Recursively parse and index subtitle text for future use.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    platforms='any',
    install_requires=['click', 'ass', 'SQLAlchemy'],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'mach3 = mach3.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
         'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
