import psycopg2
import json
from config import load_config

def get_connection():
    return psycopg2.connect(**load_config())

# ---------------- CREATE ----------------
def create_tables():
    with get_connection() as conn:
        with conn.cursor() as cur:
            with open("schema.sql") as f:
                cur.execute(f.read())
    print("Tables created")

# ---------------- ADD CONTACT ----------------
def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO contacts(name, email, birthday)
                VALUES (%s,%s,%s)
                ON CONFLICT (name) DO NOTHING;
            """, (name, email, birthday))

# ---------------- ADD PHONE ----------------
def add_phone():
    name = input("Name: ")
    phone = input("Phone: ")
    ptype = input("Type (home/work/mobile): ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL add_phone(%s,%s,%s);", (name, phone, ptype))

# ---------------- MOVE GROUP ----------------
def move_group():
    name = input("Name: ")
    group = input("Group: ")

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL move_to_group(%s,%s);", (name, group))

# ---------------- SEARCH ----------------
def search():
    q = input("Search: ")
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_contacts(%s);", (q,))
            print(cur.fetchall())

# ---------------- FILTER GROUP ----------------
def filter_group():
    g = input("Group: ")
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.name, g.name
                FROM contacts c
                JOIN groups g ON c.group_id = g.id
                WHERE g.name=%s;
            """, (g,))
            print(cur.fetchall())

# ---------------- SORT ----------------
def sort_contacts():
    print("1.Name 2.Birthday 3.Date")
    c = input("Choice: ")
    col = "name"
    if c == "2":
        col = "birthday"
    elif c == "3":
        col = "created_at"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT name,email FROM contacts ORDER BY {col};")
            print(cur.fetchall())

# ---------------- EXPORT JSON ----------------
def export_json():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.name,c.email,p.phone
                FROM contacts c
                LEFT JOIN phones p ON c.id=p.contact_id;
            """)
            data = cur.fetchall()

    with open("contacts.json","w") as f:
        json.dump(data,f)

    print("Exported")

# ---------------- IMPORT JSON ----------------
def import_json():
    with open("contacts.json") as f:
        data = json.load(f)

    with get_connection() as conn:
        with conn.cursor() as cur:
            for name,email,phone in data:
                cur.execute("""
                    INSERT INTO contacts(name,email)
                    VALUES (%s,%s)
                    ON CONFLICT(name) DO UPDATE SET email=EXCLUDED.email;
                """,(name,email))

# ---------------- MENU ----------------
def menu():
    while True:
        print("\n1.Create tables")
        print("2.Add contact")
        print("3.Add phone")
        print("4.Move to group")
        print("5.Search")
        print("6.Filter group")
        print("7.Sort")
        print("8.Export JSON")
        print("9.Import JSON")
        print("0.Exit")

        c = input("Choice: ")

        if c=="1": create_tables()
        elif c=="2": add_contact()
        elif c=="3": add_phone()
        elif c=="4": move_group()
        elif c=="5": search()
        elif c=="6": filter_group()
        elif c=="7": sort_contacts()
        elif c=="8": export_json()
        elif c=="9": import_json()
        elif c=="0": break

if __name__ == "__main__":
    menu()