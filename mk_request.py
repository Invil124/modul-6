import sqlite3


def execute_query(sql, db):
    with sqlite3.connect(db) as conn:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()


def open_sql_query(query):
    with open(query, "r") as fh:
        sql = fh.read()
        return sql


if __name__ == "__main__":
    sql = open_sql_query("query_5.sql")
    print(execute_query(sql, "study.db"))
