from setuptools import setup

setup(
    name="nyse_csv_json",
    version="0.1",
    description="conversion of nyse csv data to json data",
    url="https://github.com/Sridivya321/nyse-converter",
    author="Sridivya Bunga",
    author_email="sridivya.bunga@infolob.com",
    license="MIT",
    packages=["nyse_csv_json"],
    zip_safe=False,
    entry_points={
        "console_scripts": ["nyse=nyse_csv_json:main"],
    },
    install_requires=["dask[complete]<=2023.3.0"],
)
