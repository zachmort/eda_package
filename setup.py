from setuptools import setup, find_packages

VERSION = "1.0"
DESCRIPTION = "A function that summarizes data sets passed through it."
LONG_DESCRIPTION = ""

# Set up
setup(
    name="summarizeData"
    , version=VERSION
    , author="Zach Mortenson"
    , author_email=""
    , description=DESCRIPTION
    , packages=find_packages(where="explore_data")
    , install_requires=["numpy", "pandas", "seaborn", "twine"]
    , license="MIT"
    , package_dir={"":"explore_data"}
    , python_requires=">=3.10"
)

