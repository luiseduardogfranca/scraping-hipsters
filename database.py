class Database:

    def connect_database(self, firebase_admin, firestore):
        cred = firebase_admin.credentials.Certificate('./hipsters-podcast-firebase-adminsdk-yfybm-54f2918f97.json')
        firebase_admin.initialize_app(cred)
        return firestore.client()
  

    def insert(self, database, collection, podcast):
        return database.collection(collection).document().set(podcast)

    def delete(self, id_podcast):
        '''
        '''

    def update(self, id_podcast, podcast):
        '''
        '''
    