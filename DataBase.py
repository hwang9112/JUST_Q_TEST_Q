import sqlite3

# SQLite DB 연결 JUST_Q.db 고정
def connect_DB():
    try:
        conn = sqlite3.connect("JUST_Q.db")
        print("DB 연결성공")
        return conn
    except:
        print("DB연결 에러")

# Connection 닫기
def disconnect_DB(conn):
    try:
        conn.close()
        print("DB 연결 종료")
    except:
        print("DB 종료 에러")

# Connection 으로부터 Cursor 생성 및 반환
def CUR(conn):
    try:
        return conn.cursor()
    except:
        print("커서 생성 에러")

#쿼리 받아서 처리
def excute_Query(cur, rsv_Query):
    try:
        cur.execute(rsv_Query)
    except:
        print("Excute Error!")
        return -1