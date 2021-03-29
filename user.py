import random

from generators import namegen, phonegen, hash_key
from generators.transaction import trans_creation

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
            transaction = trans_creation(num)
            user_list.append({
                "user": self.user.gen_unique_names(names=self.username, surnames=self.usersurnames, how_many=num),
                "phone": self.phone.random_with_N_digits(7, num),
                "hash_pass": self.hash.key("00EX4145NVW:24442", num),
                "transaction_sum": transaction[0],
                "transaction_direction": transaction[1],
                "transaction_client": transaction[2],
                "transaction_type": transaction[3],
            })
            num -= 1
        return user_list


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, "
              "username TEXT, phone TEXT, hash_pass TEXT, transaction_sum TEXT, "
              "transaction_direction TEXT, transaction_client TEXT, transaction_type TEXT)")


def data_entry():
    user_create = User(10000)
    count = user_create.new_user()
    for item in count:
        print("Processing...")
        c.execute(
            "INSERT INTO Users(username, phone, hash_pass, transaction_sum, transaction_direction, transaction_client, transaction_type) "
            "VALUES(?, ?, ?, ?, ?, ?, ?)", (item.get("user"),
                                            item.get("phone"),
                                            item.get("hash_pass"),
                                            item.get("transaction_sum"),
                                            item.get("transaction_direction"),
                                            item.get("transaction_client"),
                                            item.get("transaction_type"),
                                            ))
        conn.commit()
        print("Process finished")


create_table()
data_entry()

c.close()
conn.close()
