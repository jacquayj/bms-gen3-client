import requests

class HTTPClient:
    
    def __init__(self, endpoint, auth_helper):
        self.endpoint = endpoint
        self.auth_helper = auth_helper
        
    def __getattr__(self, name):
        def _missing(path, *args, **kwargs):
            prefix = "authd_"
            if name.startswith(prefix):
                method = getattr(requests, name[len(prefix):])
                method(self.endpoint + path, *args, auth=self.auth_helper, **kwargs)
        return _missing
