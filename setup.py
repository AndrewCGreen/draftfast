import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

requires = [
    'numpy',
    'terminaltables',
    'ortools',
]

setuptools.setup(
    name='draftfast',
    version='3.3.5',
    author='Ben Brostoff',
    author_email='ben.brostoff@gmail.com',
    description='A tool to automate and optimize DraftKings and FanDuel '
                'lineup construction.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/BenBrostoff/draftfast',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=requires,
)
