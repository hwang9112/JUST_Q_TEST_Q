"""
파이썬 단독 실행시 사용
import DataBase as Database
"""
import JUST_Q_TEST_Q.DataBase as Database
import pandas as pd

#Excel 데이터 분할 및 쿼리 함수
def insert_Query(cursor, excel_data):
    # 테이블 생성 체크 쿼리
    table_check = Database.excute_Query(cursor, "select * from SampleData")
    # 테이블 체크시 테이블 없으면 생성
    if table_check == -1:
        table_query = "CREATE TABLE SampleData" \
                      "(OrderDate date, Region text, Rep text, Item text, Units num, Unit_Cost float, Total float, " \
                      "PRIMARY KEY(OrderDate, Region, Rep, Item));"
        Database.excute_Query(cursor, table_query)
        DBconn.commit()  # 커밋

    for split_data in range(len(excel_data)):
        # print(excel_data.loc[split_data])
        Q_data1 = excel_data.loc[split_data]['OrderDate']
        Q_data1 = pd.to_datetime(Q_data1) #Datetime으로 변환하기 위함
        Q_data2 = excel_data.loc[split_data]['Region']
        Q_data3 = excel_data.loc[split_data]['Rep']
        Q_data4 = excel_data.loc[split_data]['Item']
        Q_data5 = excel_data.loc[split_data]['Units']
        Q_data6 = excel_data.loc[split_data]['Unit Cost']
        Q_data7 = excel_data.loc[split_data]['Total']
        insert_query = "INSERT INTO SampleData VALUES(" \
                       "'" + str(Q_data1) + "',"  \
                       "'" + str(Q_data2) + "',"  \
                       "'" + str(Q_data3) + "',"  \
                       "'" + str(Q_data4) + "',"  \
                       + str(Q_data5) + ","  \
                       + str(Q_data6) + ","  \
                       + str(Q_data7) + ");"

        error_check = Database.excute_Query(cursor, insert_query)
        # 중복 막기 위한 error 체크
        if error_check == -1:
            DBconn.rollback()
        else:
            DBconn.commit()

#Database 쿼리 전달 및 출력 함수
def send_Query(cursor, Query):
    Query_result = Database.excute_Query(cursor, Query)
    #쿼리 결과가 에러일 경우 예외처리 위함
    if Query_result == -1:
        pass
    else:
        for DBcontents in Query_result:
            print("result = " + str(DBcontents))

# main 실행 위한 부분
if __name__ ==  '__main__':
    DBconn = Database.connect_DB() #데이터베이스 연결
    cursor_01 = Database.CUR(DBconn) #커서 생성
    #Excel 내용 불러오기
    excel_data = pd.read_excel("Sample_Data\SampleData.xlsx",sheet_name="SalesOrders")
    #Excel 내용 DB입력
    insert_Query(cursor_01, excel_data)
    send_Query(cursor_01, "SELECT * FROM SampleData") #내용 확인
    # send_Query(cursor_01, "select region from SampleData")
    # send_Query(cursor_01, "drop table SampleData") #Table 지우기
    Database.disconnect_DB(DBconn) #데이터베이스 종료






