#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # أخذ معلومات الاتصال من سطر الأوامر
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # الاتصال بقاعدة البيانات
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    cur = db.cursor()
    # تنفيذ الاستعلام
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # طباعة النتائج
    for row in cur.fetchall():
        print(row)

    # إغلاق الاتصال
    cur.close()
    db.close()
