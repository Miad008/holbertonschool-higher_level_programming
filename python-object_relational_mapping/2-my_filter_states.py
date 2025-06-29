#!/usr/bin/python3
"""
Takes an argument and displays all values in the states table
where name matches the argument (exact match).
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # أخذ بيانات الاتصال والاسم المطلوب البحث عنه
    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # الاتصال بقاعدة البيانات
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    cur = db.cursor()

    # ⚠️ استخدمنا format كما هو مطلوب (لكن هذا غير آمن ضد SQL injection)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # طباعة النتائج
    for row in cur.fetchall():
        print(row)

    # إغلاق الاتصال
    cur.close()
    db.close()
