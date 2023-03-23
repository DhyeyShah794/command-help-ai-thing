import random
import string


def gen_session_id():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))


def handle_session():
    with open('.env', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if "SessionID" in line:
                session_id = line.split("'")[1].replace("'", "")
                break
        else:
            session_id = gen_session_id()
            with open('.env', 'a') as f:
                f.write(f"\nSessionID='{session_id}'")
    return session_id
