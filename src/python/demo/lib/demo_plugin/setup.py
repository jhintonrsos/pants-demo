
import os
from setuptools import find_packages, setup


setup(
    name="pants-demo",
    description="Example pants demo",
    url="http://www.github.com",
    author="Pants",
    packages=find_packages(),
    version="2.0.1",
    entry_points={
        'pytest11': [
            'demo_plugin = demo.lib.demo_plugin.plugin'
        ],
    },
    classifiers=["Framework :: Pytest"]
)
