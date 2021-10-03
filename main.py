from gdrive_api_tools import get_authorization, upload_file

def main():
   drive = get_authorization()
   upload_file(drive, 'acc nerves.png')
   drive.close()
if __name__ == '__main__':
   main()