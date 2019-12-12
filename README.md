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

```python
from bms_gen3_client import Gen3Client

client = Gen3Client(
    "https://bms-gen3-dev.johnjacquay.com",
    api_user="my-account",
    api_pass="$2b$12$2CKlcJHgdJw0IaK.RktfveH5NFWW4KxrMFaKjPnbCdbLEJcBeDA6m"
)

# Fetch projects
projects = client.fetch_projects(limit=1000, offset=0)

# Raw GraphQL query using gen3.submission.Gen3Submission
client.submission.query("{project{code}}")

# Fetch object GUID by S3 URI
guid = client.get_guid_by_s3_uri("s3://my-bucket/my-obj.txt")

## INFO: 
# Access instantiated class 'gen3.submission.Gen3Submission' via 'client.submission'
# https://gen3sdk-python.readthedocs.io/en/latest/submission.html
#
# Access instantiated class 'gen3.file.Gen3File' via 'client.file'
# https://gen3sdk-python.readthedocs.io/en/latest/file.html


# Create a generic submission, see create_project example below for json_dict example of a project node
client.submission.submit_record(json_dict)

# Fetch the presigned AWS S3 URL for downloading data via GUID
download_url = client.file.get_presigned_url("dg.XXXX/e8dd1662-25d8-4c94-87f9-4c3d0e8d16e4")

# Create project
# https://gen3sdk-python.readthedocs.io/en/latest/submission.html
client.submission.create_project("bms_open", {
    "type": "project",
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
    "trial": "CA111-555"
})

# Arbitrary get, post, put, delete requests
dictionary = client.authd_get("/api/v0/submission/_dictionary/_all").json()
projects = client.authd_post("/api/v0/submission/graphql", json={"query":"{project{code}}"}).json()


```