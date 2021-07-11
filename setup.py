from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')
requirements_txt = (here / 'requirements.txt').read_text(encoding='utf-8')

setup(
    name='sunnah-api',
    version='0.3.0',
    description='Exposes Sunnah.com API as clean & typed dataclass objects',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/NaxAlpha/sunnah-api',
    author='Nauman Mustafa', 
    author_email='nauman.mustafa.x@gmail.com',
    classifiers=[  
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='sunnah, sunnah-com, api, wrapper',
    packages=find_packages(where='.'),
    python_requires='>=3.8, <4',
    install_requires=requirements_txt.split('\n'),

    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    # extras_require={  # Optional
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    # package_data={  # Optional
    #     'sample': ['package_data.dat'],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],  # Optional

    # entry_points={  # Optional
    #     'console_scripts': [
    #         'sunnah_api=sunnah_api:main',
    #     ],
    # },
    project_urls={  
        'Bug Reports': 'https://github.com/NaxAlpha/sunnah-api/issues',
        'Source': 'https://github.com/NaxAlpha/sunnah-api',
    },
)