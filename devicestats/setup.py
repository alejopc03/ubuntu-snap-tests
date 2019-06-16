from setuptools import setup, find_packages

setup(
    name = "device-stats",
    version = "0.1",
    #packages = find_packages(),
    py_modules=['devicestats'],
    scripts = [],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = [],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt'],
    },
    entry_points={
        'console_scripts': ['devicestats = devicestats:main']
    },

    # metadata for upload to PyPI
    author = "Alejandro Pereira Calvo",
    description = "Handles IOT device information",
    license = "",
    keywords = "",
    url = ""
)