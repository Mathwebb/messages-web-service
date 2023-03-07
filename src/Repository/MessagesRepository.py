from Repository.StandardRepository import StandardRepository


class MessagesRepository(StandardRepository):
    def __init__(self):
        super().__init__()

    def get_message(self, message_id):
        self.cursor.execute("""
                SELECT * FROM messages WHERE message_id = ?
                """, (message_id,))
        return self.cursor.fetchone()

    def get_messages(self):
        self.cursor.execute("""
                SELECT * FROM messages
                """)
        return self.cursor.fetchall()
    
    def get_messages_by_sender(self, sender_id):
        self.cursor.execute("""
                SELECT * FROM messages WHERE sender_id = ?
                """, (sender_id,))
        return self.cursor.fetchall()
    
    def get_messages_by_recipient(self, recipient_id):
        self.cursor.execute("""
                SELECT * FROM messages WHERE recipient_id = ?
                """, (recipient_id,))
        return self.cursor.fetchall()

    def insert_message(self, sender_id, recipient_id, subject, body):
        self.cursor.execute("""
                INSERT INTO messages (sender_id, recipient_id, subject, body) VALUES (?, ?, ?, ?)
                """, (sender_id, recipient_id, subject, body))
        self.conn.commit()
        return self.cursor.lastrowid

    def update_message(self, message_id, sender_id, recipient_id, subject, body):
        self.cursor.execute("""
                UPDATE messages SET sender_id = ?, recipient_id = ?, subject = ?, body = ? WHERE message_id = ?
                """, (sender_id, recipient_id, subject, body, message_id))
        self.conn.commit()

    def delete_message(self, message_id):
        self.cursor.execute("""
                DELETE FROM messages WHERE message_id = ?
                """, (message_id,))
        self.conn.commit()
