import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate("secret.json")
initialize_app(cred)

firestore_db = firestore.client()


def save_data(collection, question, answer, engine, randomness):
    firestore_db = firestore.client()
    data = {
        'question': question,
        'answer': answer,
        'engine': engine,
        'randomness': randomness,
        'timestamp': firestore.SERVER_TIMESTAMP,
        }
    firestore_db.collection(collection).add(data)
