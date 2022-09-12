import pandas as pd
import sqlite3



class Students:
    def __init__(self, adm_no, name, _class_):
        self.adm_no = adm_no
        self.name = name
        self._class_ = _class_

    def __str__(self):
        return f"Name : {self.name}, Class : {self._class_}, Admission Number : {self.adm_no}"

def insert_db(id, name, _class_):
    con = sqlite3.connect("Students.db")
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO Students values ( ?, ?, ? )",( id, name,_class_,))
        print("Executed sucessfully")
        con.commit()


        # if sql_insert.lstrip().upper().startswith("INSERT"):
        #     cur.execute(sql_insert)
    except:
        print("Something went wrong")
        con.rollback()
    con.close()

def insert_many(list_values):
    con = sqlite3.connect("Students.db")
    cur = con.cursor()
    try:
        cur.executemany("INSERT INTO Students values ( ?, ?, ? )",list_values)
        print("Executed successfully")
        con.commit()


        # if sql_insert.lstrip().upper().startswith("INSERT"):
        #     cur.execute(sql_insert)
    except Exception as e:
        print(e)
        con.rollback()
    con.close()



def update_db():
    con = sqlite3.connect("Students.db")
    cur = con.cursor()

    try:
        if sql_update.lstrip().upper().startswith("INSERT"):
            cur.execute(sql_update)

    except:
        print("Something went wrong")
        con.rollback()

    con.close()
    # return

def view():
    con = sqlite3.connect("Students.db")
    # surveys_df = pd.read_sql_query("SELECT DISTINCT class, count(*) from Students GROUP BY class", con)
    surveys_df = pd.read_sql_query("SELECT * from Students", con)
    con.close()
    return surveys_df







option = int(input("Choose Options: 1.VIEW 2.INSERT 1 3.INSERT MANY 4.UPDATE 5.DELETE :"))
if option == 1:

    std = view()
    print(std)





elif option == 2:

    insert_flag = True

    while insert_flag:
        id = input("Enter Student Admission Id : ")
        name = input("Enter Student Name: ")
        _class_ = input("Enter Student Class")

        status = input("Do You want to proceed inserting Data (y/n) :")
        if status.upper() == "Y":
            insert_db(id, name, _class_)
            state = input("Do you want to continue (y/n):")
            if state.upper() == "Y":
                continue
            else:
                quit()
        else:
            insert_flag = False

# print(Students)



elif option == 3:
    insert_flag = True
    i = 1
    list_final = []
    while insert_flag:

        input_list_1 = input(f"Provide the Admission number for student {i}: ")
        input_list_2 = input(f"Provide the Name for student {i}: ")
        input_list_3 = input(f"Provide the Class for student {i}: ")

        input_list = (input_list_1,input_list_2,input_list_3)
        print(f"Name : {input_list_2}, Admission Number : {input_list_1}, Class : {input_list_3}")
        status = input("Do you want to insert more values (y/n):")
        list_final.append(input_list)

        if status.upper() == "Y":
            i +=1

            continue
        else:
            insert_many(list_final)
            print("Execution Completed. PLease run the script again to insert more data")
            break






# else:
#     pass
#
# sql_insert = str(input())
# sql_insert = sql_insert.strip()
# sql_update = str(input())
# df = pd.DataFrame()





#
# # con = sqlite3.connect("Students.db")
# con = sqlite3.connect("Students.db")
# # surveys_df = pd.read_sql_query("SELECT * from Students", con)
# # surveys_df = pd.read_sql_query("SELECT DISTINCT class, count(*) from Students GROUP BY class", con)
# # print(surveys_df)
#
# cur = con.cursor()
#
# sql0 = "DROP TABLE IF EXISTS Students"
#
# sql1 = """
#         CREATE TABLE Students
#         ( admID INT,
#         name varchar,
#         class varchar,
#         primary key (admID))
#         """
# cur.execute(sql0)
# cur.execute(sql1)
#
# cur.execute("INSERT INTO Students values (28,'Juti','II')")

# for row in cur.execute('SELECT * FROM Students'):
#     print(row)

# cur.execute('SELECT * FROM Students WHERE class = "I"')
# cur.fetchone()

#
# con.commit()
# con.close()
