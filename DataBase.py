import sqlite3

# SQLite DB 연결 JUST_Q.db 고정
def connect_DB():
    try:
        conn = sqlite3.connect("JUST_Q.db")
        print("DB Connect Success")
        return conn
    except:
        print("DB Connect Error")

# Connection 닫기
def disconnect_DB(conn):
    try:
        conn.close()
        print("DB Disonnect ")
    except:
        print("DB Disconnect Error")

# Connection 으로부터 Cursor 생성 및 반환
def CUR(conn):
    try:
        return conn.cursor()
    except:
        print("Cursor Create Error")

#쿼리 받아서 처리
def excute_Query(cur, rsv_Query):
    try:
        cur.execute(rsv_Query)
    except:
        print("Query Excute Error")
        return -1 #에러 확인용 -1 리턴