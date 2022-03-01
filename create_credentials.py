#!/bin/env python3

import boto3
import os

credential_path = os.path.expanduser('~/.aws/credentials')

if os.path.isfile(credential_path):
    os.remove(credential_path)

credentials = boto3.Session().get_credentials()
print(credentials.access_key)
print(credentials.secret_key)
print(credentials.token)

with open(credential_path, 'w') as f:
    f.write('[default]\naws_access_key_id = %s\naws_secret_access_key = %s\naws_session_token = %s' % (credentials.access_key, credentials.secret_key, credentials.token))

