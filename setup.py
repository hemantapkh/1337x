import setuptools

with open("README.md", encoding="utf8") as fh:
    readme = fh.read()

setuptools.setup(
    name="1337x",
    version="1.0.0.tor",
    author="LeGeRyChEeSe",
    author_email="kilian.douarinou41@gmail.com",
    description="Unofficial API of 1337x.to with Tor implementation",
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=["requests", "requests[socks]", "requests[security]", "bs4", "requests-cache", "fake_useragent", "stem"],
    url="https://github.com/LeGeRyChEeSe/1337x",
    project_urls={
        "Documentation": "https://github.com/LeGeRyChEeSe/1337x/blob/main/README.md",
        "Issue tracker": "https://github.com/LeGeRyChEeSe/1337x/pulls",
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
