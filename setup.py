from setuptools import setup, find_packages


with open("README.md") as file:
    readme = file.read()

setup(
    name="yolo",
    version="0.1.0",
    description="This is a YOLOV5 wrapper.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="datascone",
    author_email="admin@datascone.com",
    url="",
    classifiers=[
        "Programming Language :: Python 3.6",
        "Programming Language :: Python 3.7",
        "Programming Language :: Python 3.8",
    ],
    package_dir={
        "": "src/yolo"
    },
    package_data={
        "": [

        ]
    },
    packages=find_packages(where="src/yolo"),
    include_package_data=True,
    install_requires=[

    ],
    python_requires=">=3.6, <4",
)
