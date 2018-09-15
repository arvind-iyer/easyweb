from setuptools import setup, find_packages

setup(
    name="easyweb",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={"console_scripts": ["easyweb = easyweb.test:main"]},
    install_requires=["Flask==1.0.2"],
)
