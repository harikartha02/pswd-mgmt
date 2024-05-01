# fire.py

def initialize_firebase():
    import firebase_admin
    from firebase_admin import credentials, storage
    if not firebase_admin._apps:
        # Initialize Firebase Admin
        cred = credentials.Certificate('C:/Users/karth/Downloads/new-proj-366e3-firebase-adminsdk-obezw-0aaeeae22f.json')
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'new-proj-366e3.appspot.com'
        })

    # Get a reference to the storage service
    bucket = storage.bucket()

    return bucket