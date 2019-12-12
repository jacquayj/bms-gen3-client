import requests
from gen3.auth import Gen3Auth
from gen3.submission import Gen3Submission
from gen3.file import Gen3File
from bms_gen3_client.base import HTTPClient

class Gen3Client(HTTPClient):
    
    def __init__(self, endpoint, api_user = '', api_pass = '', creds_json_file = '', **kwargs):
        endpoint = endpoint.rstrip("/")

        if creds_json_file == '':
            auth_helper = requests.auth.HTTPBasicAuth(api_user, api_pass)
        else:
            auth_helper = Gen3Auth(endpoint, refresh_file = creds_json_file, **kwargs)

        self.dict = None
        self.submission = Gen3Submission(endpoint, auth_helper)
        self.file = Gen3File(endpoint, auth_helper)

        super().__init__(endpoint, auth_helper)

    # Possible duplicate in self.submission
    def dictionary(self):
        if self.dict == None:
            self.dict = self.authd_get(
                "/api/v0/submission/_dictionary/_all"
            ).json()
        return self.dict
    
    # Possible duplicate in self.submission
    def query(self, graphql, g_vars = None):
        return self.authd_post(
            "/api/v0/submission/graphql/",
            json={
                "query": graphql,
                "variables": g_vars
            }
        )

    def fetch_projects(self, limit = 1000, offset = 0):
        project_fields = list(self.dictionary()['project']['properties'].keys())
        project_fields.remove('programs')

        field_str = ''.join(f + "\n" for f in project_fields)

        q = '''
            {{
                project(first:{0} offset:{1}) {{
                    {2}
                }}
            }}
        '''.format(limit, offset, field_str)

        resp = self.query(q)

        return resp.json()['data']['project']

    def get_guid_by_s3_uri(self, s3uri):
        return self.authd_get(
            "/index/_query/urls/q",
            params=[('include', s3uri)]
        ).json()[0]["did"]
    
    