from typing import Dict

class EmailAlreadyExists(Exception):
    def __init__(self, message: Dict[str, str] = { 'message': 'Email already exists' }, http_code: int = 409):
        self.message = message
        self.http_code = http_code

class NotFoundFranchisor(Exception):
    def __init__(self, message: Dict[str,str] = { 'message': 'Franchisor not found' }, http_code: int = 404):
        self.message = message
        self.http_code = http_code

class NotFoundPeople(Exception):
    def __init__(self, message: Dict[str,str] = { 'message': 'People not found' }, http_code: int = 404):
        self.message = message
        self.http_code = http_code

class NotFoundBodyRequest(Exception):
    def __init__(self, message: Dict[str,str] = { 'message': 'Body not found in request payload' }, http_code: int = 400):
        self.message = message
        self.http_code = http_code