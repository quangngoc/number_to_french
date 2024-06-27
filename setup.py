from setuptools import setup, find_packages

setup(
    name="number_to_french",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "number-to-french=number_to_french.number_to_french:main",
        ],
    },
    author="Quang Ngoc DUONG",
    author_email="quangngoc88@gmail.com",
    description="A package that converts numbers to French words",
    url="https://github.com/quangngoc/number_to_french",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
)
