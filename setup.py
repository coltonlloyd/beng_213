from setuptools import setup, find_packages


setup(name="beng_213",
      version="",
      author="Colton Lloyd",
      url="https://github.com/coltonlloyd/qbio",
      packages=find_packages(),
      install_requires=["six", "cobra", "pandas", "scipy", "sklearn",
                        "setuptools", "graphviz", "pydotplus", "seaborn",
                        "matplotlib", "escher"],
      )
