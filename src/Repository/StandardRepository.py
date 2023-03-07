import sqlite3

class StandardRepository:
    sqlite_file = 'mydb.sqlite'
    conn = None
    cursor = None

    def __init__(self):
        self.conn = sqlite3.connect(self.sqlite_file)
        self.conn.execute('PRAGMA foreign_keys = ON')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER NOT NULL PRIMARY KEY,
                        name TEXT NOT NULL,
                        email_address TEXT NOT NULL UNIQUE
                );
                """)
        self.conn.commit()

        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                        message_id INTEGER NOT NULL PRIMARY KEY,
                        sender_id INTEGER NOT NULL,
                        recipient_id INTEGER NOT NULL,
                        subject TEXT NOT NULL,
                        body TEXT NOT NULL,
                        FOREIGN KEY (sender_id)
                                REFERENCES users (user_id)
                                        ON DELETE SET NULL
                                        ON UPDATE SET NULL,
                        FOREIGN KEY (recipient_id)
                                REFERENCES users (user_id)
                                        ON DELETE SET NULL
                                        ON UPDATE SET NULL
                );
                """)
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()
