
import os
from setuptools import find_packages, setup


def get_version():
    current_dir = os.path.dirname(os.path.realpath(__file__))

    return open(
        os.path.abspath(os.path.join(current_dir, 'VERSION'))
    ).read().strip()


setup(
    name="pants-demo",
    description="Example pants demo",
    url="http://www.github.com",
    author="Pants",
    packages=find_packages(),
    version=get_version(),
    entry_points={
        'pytest11': [
            'demo_plugin = demo.lib.demo_plugin.plugin'
        ],
    },
    classifiers=["Framework :: Pytest"]
)
