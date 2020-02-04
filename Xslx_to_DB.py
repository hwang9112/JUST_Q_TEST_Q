import JUST_Q_TEST_Q.DataBase as Database
import pandas as pd


DBconn = Database.connect_DB() #데이터베이스 연결
cursor = Database.CUR(DBconn) #커서 생성

table_check = Database.excute_Query(cursor,"select * from SampleData") #테이블 생성 체크 쿼리
#테이블 체크, 테이블 없으면 생성
if table_check == -1:
    table_query = "CREATE TABLE SampleData" \
                  "(OrderDate date, Region text, Rep text, Item text, Units num, Unit_Cost float, Total float, " \
                  "PRIMARY KEY(OrderDate, Region, Rep, Item));"
    Database.excute_Query(cursor, table_query)
    DBconn.commit() #커밋 필수

#Excel 불러와서 변수에 저장
excel_data = pd.read_excel("Sample_Data\SampleData.xlsx",sheet_name="SalesOrders")

#Excel 데이터 입력 쿼리
for split_data in range(len(excel_data)):
    # print(excel_data.loc[split_data])
    Q_data1 = excel_data.loc[split_data]['OrderDate']
    Q_data1 = pd.to_datetime(Q_data1) #Date타입 변환용
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
    # print(insert_query)
    Database.excute_Query(cursor, insert_query)
    DBconn.commit()


#Excel 데이터 확인 쿼리
Database.excute_Query(cursor, "SELECT * FROM SampleData")
for a in cursor.fetchall():
    print(a)
Database.disconnect_DB(DBconn) #데이터베이스 종료






