from source.database.main import sql, db


def create_database():
    sql.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id BIGINT,
    nicknames TEXT,
    count_messages INT DEFAULT 0,
    time_in_voice INT DEFAULT 0,
    xp INT DEFAULT 0,
    rank INT DEFAULT 0,
    date BIGINT)""")
    db.commit()


def get_user_by_id(user_id):
    sql.execute("SELECT * FROM users WHERE id = ?", [user_id])
    return sql.fetchone()


def create_user(user_name):
    sql.execute(
        "INSERT INTO users VALUES (?,0,0)", [user_name])
    db.commit()


def update_voice_time(user_id, time):
    """

        @param
        user_id
        user
        id

        @param
        time in second, will
        be
        added
        to
        user
        voice
        time


    """
    sql.execute(
        "UPDATE users SET time_in_voice = time_in_voice + ? WHERE id = ?", [time, user_id])
    db.commit()


def update_message_count(user_id, count=1):
    """

        @param
        user_id
        user
        id

        @param
        count
        messages


    """
    sql.execute(
        "UPDATE users SET count_messages = count_messages + ? WHERE id = ?", [count, user_id])
    db.commit()


def update_user_xp(user_id, xp=0):
    """

        @param
        user_id
        user
        id

        @param
        count
        messages


    """
    if xp > 0:
        sql.execute(
            "UPDATE users SET xp = v + ? WHERE id = ?", [xp, user_id])
        db.commit()
