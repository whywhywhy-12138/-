#!/usr/bin/python

import sqlite3


class faceData():
    def __init__(self):
        self.conn = sqlite3.connect('test.db',check_same_thread=False)
        self.c = self.conn.cursor()
        self.c.execute(''' CREATE TABLE IF NOT EXISTS face_data
               (ID INT PRIMARY KEY     NOT NULL,
               NAME           TEXT    NOT NULL);''')

    def __del__(self):
        self.data_close()

    def face_insert(self,name):
        max=self.id_MAX()
        curr_id=1
        if max:
            curr_id+=max
        self.c.execute("INSERT INTO face_data (ID,NAME) \
                        VALUES ("+str(curr_id)+", '"+str(name)+"' )")
        print(curr_id)
        self.conn.commit()

    def id_MAX(self):
        data_cu=self.c.execute("SELECT max(ID) FROM face_data")
        for row in data_cu:
            return row[0]

    def face_get(self,id):
        for row in self.c.execute("SELECT NAME FROM face_data WHERE ID="+str(id)):
            return row[0]

    def face_del(self):
        self.c.execute("DELETE from face_data;")
        self.conn.commit()

    def data_close(self):
        self.c.close()
        self.conn.close()
