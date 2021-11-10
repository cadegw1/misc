from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']


class Drive:
    def __init__(self):
        """
        Init function for Drive class which handles authorization and establishing a session
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self._service = build('drive', 'v3', credentials=creds)

    def list_items(self, file_type='files', query_string=''):
        """
        Lists all files that contain the query string and correspond to the file type
        :param file_type: file type specification that determines the correct query string
        :param query_string: string that function searches for in files
        :return: True if files were returned else False
        """
        page_token = None
        file_queries = {
            'files': "name contains '{}'and mimeType != 'application/vnd.google-apps.folder'",
            'folders': "name contains '{}' and mimeType = 'application/vnd.google-apps.folder'"
        }
        if file_type == 'files':
            query_string = file_queries['files'].format(query_string)
        elif file_type == 'folders':
            query_string = file_queries['folders'].format(query_string)
        else:
            print("Error: Invalid query string")
            return False
        results = self._service.files().list(q=query_string,
                                             spaces='drive',
                                             fields='nextPageToken, files(id, name)',
                                             pageToken=page_token).execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return False
        else:
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))
        return True


if __name__ == '__main__':
    import code
    D = Drive()
    code.interact(local=locals())
