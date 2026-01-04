from setuptools import setup

setup(
    name="hardware-panel",
    version="1.0.0",
    author="Martim 'martimmpr' Ribeiro",
    description="Powerful system monitoring and hardware control application for Linux with real-time monitoring and power profile management.",
    url="https://github.com/martimmpr/linux-hardware-panel",
    py_modules=["hardware_panel"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Hardware",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PyQt5>=5.15.0",
        "psutil>=5.8.0",
        "pyqtgraph>=0.12.0",
    ],
    entry_points={
        "console_scripts": [
            "hardware-panel=hardware_panel:main",
            "hwpanel=hardware_panel:main",
        ],
    },
)