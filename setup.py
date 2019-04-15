from setuptools import setup

import spotiboi

with open("README.md", encoding="utf8") as f:
    readme = f.read()

setup(
    name="spotiboi",
    version=spotiboi.__version__,
    description="Emulate Spotify's premium features.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Gurtej Saini",
    author_email="gxrtej@gmail.com",
    url="https://github.com/grrtej/spotiboi",
    keywords="spotify blocker",
    license="GPLv3",
    packages=["spotiboi"],
    install_requires=["pygobject", "pydbus", "pulsectl"],
    extras_require={"dev": ["black==19.3b0", "pylint"]},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
    ],
    entry_points={"console_scripts": ["spotiboi = spotiboi.spotiboi:main"]},
)
