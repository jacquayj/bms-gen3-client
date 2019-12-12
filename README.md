# bms-gen3-client

Includes API client wrapper for Gen3, supporting HTTP basic auth and eternal API keys.

## Features

- Eternal API keys via basic HTTP auth
- Fetch projects data from Gen3 via Peregrine (Graph Model)

## Install

### Fetch code

```
$ git clone https://github.com/jacquayj/bms-gen3-client.git
$ cd bms-gen3-client
```

### (optional) Create virtual environment

```
$ python3 -m venv .venv
$ source .venv/bin/activate
```

### Installation

```
$ pip install -r requirements.txt
$ python setup.py install
```

## Usage

See `Scripts/` directory for more example code.

```python
from bms_gen3_client import Gen3Client

client = Gen3Client(
    "https://bms-gen3-dev.johnjacquay.com",
    api_user="my-account",
    api_pass="$2b$12$2CKlcJHgdJw0IaK.RktfveH5NFWW4KxrMFaKjPnbCdbLEJcBeDA6m"
)

# Fetch projects
projects = client.fetch_projects(limit=1000, offset=0)

# Fetch GUID by S3 URI
guid = client.get_guid_by_s3_uri("s3://my-bucket/my-obj.txt")

# Create project
# https://gen3sdk-python.readthedocs.io/en/latest/submission.html
client.submission.create_project("bms_open", {
    "availability_type": "Restricted",
    "collaborators": [],
    "data_provider": "ABI",
    "dbgap_accession_number": "na",
    "indication": "Lung",
    "investigator_name": "fghj",
    "molecular_analysis_method": "Cytogenetics, NOS",
    "name": "dfgj",
    "project_barcode": "na",
    "project_description": "fghj",
    "project_type": "Non Clinical",
    "therapeutic_area": "Atherosclerosis NOS",
    "translational_program": "IPF",
    "trial": "CA111-555",
    "type": "project"
})

# Create a generic submission
# https://gen3sdk-python.readthedocs.io/en/latest/submission.html
client.submission.submit_record(json)

# Fetch the presigned AWS S3 URL for downloading data via GUID
# https://gen3sdk-python.readthedocs.io/en/latest/file.html
download_url = client.file.get_presigned_url("dg.XXXX/e8dd1662-25d8-4c94-87f9-4c3d0e8d16e4")


```