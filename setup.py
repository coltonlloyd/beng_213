from setuptools import setup, find_packages


setup(name="beng213",
      version="",
      author="Colton Lloyd",
      url="https://github.com/coltonlloyd/beng_213",
      packages=find_packages(),
      install_requires=["six", "cobra", "pandas", "scipy",
                        "setuptools",  "seaborn",
                        "matplotlib", "escher"],
      )
