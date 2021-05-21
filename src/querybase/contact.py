from library.db.mysql_db import Database

db = Database()


class Contact:

    @staticmethod
    def concerns(name, email, message):
        query = f"""
            INSERT INTO contact_us
                (name, email, message)
                VALUES('{name}', '{email}', '{message}');
            """
        return db.insert(query)
