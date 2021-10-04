""" Contains various functions to work with the Google Drive API.
"""

from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/drive.file'
CLIENT_SECRET = 'client_secret.json'
HTTP_OK = 200

def get_authorization() -> discovery.Resource:
    """ Executes the OAuth2Client flow. 

        Returns:
            A googleapiclient.discovery.Resource object that has authorization
            to be accessed.
    """
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        oauth_flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
        creds = tools.run_flow(oauth_flow, store)
    DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))
    return DRIVE

def upload_file(drive_service, filename) -> None:
    """ Uploads the file specified to the service provided. """
    metadata = {'name': filename}
    result = drive_service.files().create(body=metadata, media_body=filename).execute()
    if result:
        print('Successfully uploaded "%s" (%s)' % (filename, result['mimeType']))