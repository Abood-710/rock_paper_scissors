try:
    from setuptools import setup
except ImportError as error:
    from distutils.core import setup

name = "RockPaperScissors"
version = "1.0"

setup(
    name=name,
    version=version,
    description="control the RockPaperScissors device",
    author="Abdullah Al-Rumaithah",
    author_email="aboodagl710@gmail.com",
    maintainer=" You! ",
    url="https://git.yseq.net:3333/abdullah/RockPaperScissors",
    py_modules=['rock_paper_scissors'],
    zip_safe=False,
    install_requires=[],
    provides=[
        "{} ({})".format(name, version),
    ],
)
