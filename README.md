# YOLO Package

This is a wrapper repository to use the YOLOv5 implementation as a python package.

## Setup

Clone this repo and the submodules:

```commandline
$ git clone --recurse-submodules --remote-submodules git@github.com:datascone/yolo-pkg.git
```

Create and activate a virtualenv:
* `python3 -m virtualenv venv`
* `source venv/bin/activate`

Install requirements and package:
* `pip install -r requirements.txt`
* `pip install -e .`
