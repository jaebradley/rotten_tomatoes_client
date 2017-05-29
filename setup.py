from setuptools import setup, find_packages
setup(
  name="rotten_tomatoes_client",
  packages=find_packages(exclude=['tests*']),
  install_requires=["requests", "enum34"],
  version="0.0.3",
  description="Rotten Tomatoes Client",
  author="Jae Bradley",
  author_email="jae.b.bradley@gmail.com",
  url="https://github.com/jaebradley/rotten_tomatoes_client",
  download_url="https://github.com/jaebradley/rotten_tomatoes_client/tarball/0.1",
  keywords=["rotten_tomatoes"],
  classifiers=[],
)