#setup.py

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    fh.close()

setuptools.setup(
    name="analysis-k-nagai", # Replace with your own username
    version="0.0.1",
    author="Keigo Nagai",
    author_email="keigonagai@gmail.com",
    description="Analysis package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)