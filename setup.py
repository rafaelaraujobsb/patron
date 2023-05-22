import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="patron",
    version="0.0.1",
    author="Rafael Araujo",
    author_email="bsb.rafaelaraujo@gmail.com",
    description="Gerenciador de importação",
    url="https://github.com/rafaelaraujobsb/patron",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pymongo==3.5.1',
        'flask-restful==0.3.7',
        'flask==1.0.3',
        'flasgger==0.9.2',
        'loguru==0.2.5',
        'requests==2.31.0'
    ]
)