import setuptools

setuptools.setup(
    name="csv_labeler",
    version="0.1.0",
    author="Julianna",
    author_email="holleyju@uchicago.edu",
    description="Load a CSV, drop the row-number column, and add a label column",
    packages=setuptools.find_packages(),
    install_requires=[
        "pandas",
    ],
)