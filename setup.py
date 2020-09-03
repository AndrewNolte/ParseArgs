import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="parseargs", # Replace with your own username
    version="0.0.5",
    author="Andrew Nolte",
    author_email="anolte512@gmail.com",
    description="A simple package for parsing function arguments from the command line",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AndrewNolte/ParseArgs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

