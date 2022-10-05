from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'nbapi is an open source python library that acts as an API wrapper for National Bank Direct Brokerage.'

# Setting up
setup(
    name="nbapi",
    version=VERSION,
    author="Andre Ceschia",
    author_email="andre.ceschia04@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['cloudscraper'],
    keywords=['python', 'finance', 'national bank direct brokerage', 'national bank of canada', 'broker api', 'nbdb'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)