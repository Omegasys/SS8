from setuptools import setup, find_packages

setup(
    name="secure-ss7-simulator",
    version="0.1.0",
    description="A secure, user-notifying simulation of SS7-like signaling networks.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/secure-ss7-simulator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "asyncio",
        "websockets",
        "cryptography",
        "pyjwt",
        "loguru",
        "pydantic",
        "requests",
        "pytest",
        "pytest-asyncio",
        "python-dotenv",
        "rich",
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "run-simulation=core.signaling:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Communications :: Simulation",
        "Intended Audience :: Developers",
    ],
    license="GPLv3",
    include_package_data=True,
    zip_safe=False,
)
