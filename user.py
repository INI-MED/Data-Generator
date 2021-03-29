import random

from generators import namegen, phonegen, hash_key

import sqlite3

conn = sqlite3.connect('Users.db')
c = conn.cursor()


class User:

    def __init__(self, nums):
        self.nums = nums
        self.user = namegen
        self.phone = phonegen
        self.hash = hash_key
        self.username = namegen.names
        self.usersurnames = namegen.surnames

    def new_user(self):
        num = self.nums
        user_list = []
        if num <= 0:
            print("wrong number")

        while num >= 1:
            user_list.append({
                "user": self.user.gen_unique_names(names=self.username, surnames=self.usersurnames, how_many=num),
                "phone": self.phone.random_with_N_digits(7, num),
                "hash_pass": self.hash.key("00EX4145NVW:24442", num),
            })
            num -= 1
        return user_list


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, username TEXT, phone TEXT, hash_pass TEXT)")


def data_entry():
    user_create = User(10000)
    count = user_create.new_user()

    for item in count:
        print("Processing...")
        c.execute("INSERT INTO Users(username, phone, hash_pass) VALUES(?, ?, ?)", (item.get("user"),
                                                                                    item.get("phone"),
                                                                                    item.get("hash_pass"),))
        # c.execute("INSERT INTO Users (username) VALUES (?)", (item.get("user"),))
        # c.execute("INSERT INTO Users (phone) VALUES (?)", (item.get("phone"),))
        # c.execute("INSERT INTO Users (hash) VALUES (?)", (item.get("hash"),))
        # c.execute("INSERT INTO Users (id) VALUES (?)", (item.get("id"),))
        conn.commit()
        print("Process finished")


create_table()
data_entry()

c.close()
conn.close()
