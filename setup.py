from setuptools import setup

setup(
    name="Flasked-Docs",
    version="0.0.3",
    packages=["flasked_docs"],
    url="",
    license="AGPLv3",
    author="Koen van Eijk",
    author_email="vaneijk.koen@gmail.com",
    install_requires=["flask", "markdown"],
    package_data={"flasked_docs": ["templates/*", "static/*"]},
)
