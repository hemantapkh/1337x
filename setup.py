import setuptools

with open("README.md", encoding="utf8") as f:
    readme = f.read()
    
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="1337x",
    version="1.2.5",
    author="Hemanta Pokharel",
    author_email="hemantapkh@yahoo.com",
    description="Unofficial API of 1337x.to",
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    url="https://github.com/hemantapkh/1337x",
    project_urls={
        "Documentation": "https://github.com/hemantapkh/1337x/blob/main/README.md",
        "Issue tracker": "https://github.com/hemantapkh/1337x/issues",
      },
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    python_requires='>=3.0',
)
