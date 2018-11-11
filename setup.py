import setuptools

with open('README.md', 'r') as readmeFile:
    long_description = readmeFile.read()

setuptools.setup(
    name='pygeodesic',
    version='0.0.1',
    author='Isaac Waldron',
    author_email='isaac@waldronis.com',
    description='A minimal framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/isaacwaldron/pygeodesic',
    packages=setuptools.find_packages(
        include=['pygeodesic']
    ),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent'
    ]
)
