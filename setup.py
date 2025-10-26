from setuptools import setup, find_packages

setup(
    name="byteSnap",                 
    version="0.1.0",                 
    packages=find_packages(),        
    install_requires=[],             
    python_requires='>=3.7',        
    description="A utility to manage image files by creating folders and copying them.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/ft.yama/byteSnap", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
