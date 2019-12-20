from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="bms-gen3-client",
    version="0.0.4",
    description="Gen3 client wrapper for HTTP basic auth and eternal API keys for BMS",
    url="https://github.com/jacquayj/bms-gen3-client", # Need to rehost at GitHub
    license="Apache",
    install_requires=requirements,
    packages=find_packages(),
)
