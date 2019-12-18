from setuptools import setup, find_packages

setup(
    name="bms-gen3-client",
    version="0.0.4",
    description="Gen3 client wrapper for HTTP basic auth and eternal API keys for BMS",
    url="https://github.com/jacquayj/bms-gen3-client", # Need to rehost at GitHub
    license="Apache",
    # entry_points={
    #     'console_scripts': [
    #         'bms_load_projects=bms_project_morph:load_projects',
    #     ],
    # },
    packages=find_packages(),
)
