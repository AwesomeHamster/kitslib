import pathlib
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setuptools.setup(
    name="kitslib",
    version="0.0.1",
    description="Common library for kitsunebi",
    long_description=README,
    long_description_content_type="text/x-markdown",
    author="Maiko Tan",
    author_email="maiko.tan.coding@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7"
)
