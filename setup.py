from setuptools import setup, find_packages

setup(
    name="codetree-cli",
    version="0.2.2",
    author="Reza Mardani", 
    author_email="mardanireza30@gmail.com",
    description="A tool for counting lines of code in a project.", 
    long_description=open("README.md").read(), 
    long_description_content_type="text/markdown", 
    url="https://github.com/rezamardaniDev/codetree.git",  
    packages=find_packages(), 
    classifiers=[ 
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6', 
    install_requires=[  
    ],
    entry_points={  
        'console_scripts': [
            'codetree=codetree.cli:main',
        ],
    },
)
