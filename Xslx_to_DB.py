import JUST_Q_TEST_Q.DataBase as Database
import pandas as pd


DBconn = Database.connect_DB() #데이터베이스 연결
cursor = Database.CUR(DBconn) #커서 생성

table_check = Database.excute_Query(cursor,"select * from SampleData") #테이블 생성 체크 쿼리
#테이블 체크, 테이블 없으면 생성
if table_check == -1:
    table_query = "CREATE TABLE SampleData" \
                  "(OrderDate date, Region text, Rep text, Item text, Units num, Unit_Cost float, Total float);"
    Database.excute_Query(cursor, table_query)
    DBconn.commit() #커밋 필수
table_check = Database.excute_Query(cursor,"select * from SampleData") #테이블 생성 체크 쿼리
#Excel 불러와서 변수에 저장
excel_data = pd.read_excel("Sample_Data\SampleData.xlsx",sheet_name="SalesOrders")
print(excel_data)
#Excel 데이터 입력 쿼리
#Excel 데이터 확인 쿼리
Database.disconnect_DB(DBconn) #데이터베이스 종료






