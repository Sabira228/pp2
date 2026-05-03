import psycopg2
from config import load_config

def get_connection():
    return psycopg2.connect(**load_config())


def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS leaderboard (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50),
                    score INT
                )
            """)


def insert_score(name, score):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO leaderboard(name, score) VALUES (%s, %s)",
                (name, score)
            )


def get_leaderboard():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name, score FROM leaderboard ORDER BY score DESC LIMIT 10")
            return cur.fetchall()