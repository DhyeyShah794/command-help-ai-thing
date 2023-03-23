import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate("secret.json")
initialize_app(cred)

firestore_db = firestore.client()
# song = input("Enter the name of the song: ")
# artist = input("Enter the name of the artist: ")
# song = "The Sound of Silence"
# artist = "Simon & Garfunkel"
# firestore_db.collection('songs').add({'song': song, 'artist': artist})
# snapshots = list(firestore_db.collection('songs').get())
# for snapshot in snapshots:
#     print(snapshot.to_dict())

def add_question_answer(collection, question, answer, engine, randomness):
    firestore_db = firestore.client()
    data = {
        'question': question,
        'answer': answer,
        'engine': engine,
        'randomness': randomness,
        'timestamp': firestore.SERVER_TIMESTAMP,
        }
    firestore_db.collection(collection).add(data)
