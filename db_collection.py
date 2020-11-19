import pandas as pd
df = pd.read_csv("train_lyrics_1000.csv")


list = df.columns
df1 = pd.DataFrame(columns = list)
df1 = df1.append(df[df['mood'] == 'sad'])
list = df.columns
df2 = pd.DataFrame(columns = list)
df2 = df2.append(df[df['mood'] == 'happy'])
sad = df1.head(10)
happy = df2.head(10)

import psycopg2

try:
   connection = psycopg2.connect(user="PostgreSQL 12",
                                  password="1234",
                                  host="127.0.0.1",
                                  port="63775",
                                  database="krunal")
   cursor = connection.cursor()

   postgres_insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s,%s,%s)"""
   record_to_insert = (5, 'One Plus 6', 950)
   cursor.execute(postgres_insert_query, record_to_insert)

   connection.commit()
   count = cursor.rowcount
   print (count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")