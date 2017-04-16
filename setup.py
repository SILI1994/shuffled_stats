from distutils.core import setup

setup(
    name = 'shuffled_stats',
    version = '1.0.2',
    description = 'Python library for performing inference on datasets with shuffled labels',
    author = 'Abubakar Abid',
    author_email = 'a12d@stanford.edu',
    url = 'https://github.com/abidlabs/shuffled-stats', 
    download_url = 'https://github.com/abidlabs/shuffled-stats/archive/1.0.2.tar.gz',
    py_modules=['shuffled-stats'],
    keywords = ['statistics', 'shuffled', 'permutation','regression'],
    install_requires=[
        'numpy',
        'scipy',
    ],
)