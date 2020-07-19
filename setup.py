import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='Twimer', # Replace with your own username
    version='0.0.1',
    author='Moein Owhadi Kareshk',
    author_email='moein.owhadi@gmail.com',
    description='Stream Tweets into Your Favorite Databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/owhadi/twimer',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)