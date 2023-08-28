from setuptools import setup

setup(
    name="dev_aberto_cicerotcv",
    version="0.1",
    packages=["dev_aberto"],
    author="Cicero Valentim",
    author_email="elm.tiago@gmail.com",
    install_requires=["requests"],
    scripts=["scripts/hello.py"],
)
