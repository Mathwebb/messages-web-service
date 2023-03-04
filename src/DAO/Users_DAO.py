from DAO.Standard_DAO import StandardDAO

class Users_DAO(StandardDAO):
    def __init__(self):
        super().__init__()

    def get_user(self, user_id):
        self.cursor.execute("""
                SELECT * FROM users WHERE user_id = ?
                """, (user_id,))
        return self.cursor.fetchone()

    def get_user_by_email(self, email_address):
        self.cursor.execute("""
                SELECT * FROM users WHERE email_address = ?
                """, (email_address,))
        return self.cursor.fetchone()

    def get_all_users(self):
        self.cursor.execute("""
                SELECT * FROM users
                """)
        return self.cursor.fetchall()

    def insert_user(self, name, email_address):
        self.cursor.execute("""
                INSERT INTO users (name, email_address) VALUES (?, ?)
                """, (name, email_address))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_user(self, user_id, name, email_address):
        self.cursor.execute("""
                UPDATE users SET name = ?, email_address = ? WHERE user_id = ?
                """, (name, email_address, user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        self.cursor.execute("""
                DELETE FROM users WHERE user_id = ?
                """, (user_id,))
        self.conn.commit()