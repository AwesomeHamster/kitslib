from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

packages = find_packages(include=('kitslib', 'kitslib.*'))

setup(
    name="kitslib",
    version="0.0.1",
    url='https://github.com/AwesomeHamster/kitslib',
    description="Common library for kitsunebi",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Maiko Tan",
    author_email="maiko.tan.coding@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=packages,
    python_requires=">=3.7",
    platforms = ['nt', 'posix', 'os2'],
    install_requires=['aiohttp>=3.6.2'],
)
