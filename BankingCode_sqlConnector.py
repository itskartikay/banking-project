import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",passwd="1234",database="puru")
cursor=mycon.cursor()

def main():
    c=input("do you want to see the main menu? ")
    if c=='y':
        while c=='y':
            print("1.Employee Table 2. Database Table 3. Query 4.Exit")
            x=int(input("Enter Ur  choice"))
            if x==1:
                Employee()
            elif x==2:
                Database()
            elif x==3:
                QUERY()

            elif x==4:
                print("Exit")
                break
            else:
                print("not a choice ")
    else:
        print("okay")
def Employee():
    x=input("does the table exist?(If yes press enter.if no press n): ")
    if x =='n':
        cursor.execute("create table emply(S_No integer(45), E_No integer(7),E_Name varchar(45),F_Name varchar(45), M_Name varchar(45), Address varchar(125), Age integer(3), depart varchar(38), DOB date, DOJ date,P_No integer(20), Head varchar(45), Gender varchar(5), Pay integer(10))")


      #emply= table employee
       #e_no= employee number
        #E_name= employee name
        #f_name= father's name
        #m_name= mother's name



    def menu():
        if c=='y':
            while c=='y':

                print("1.Add")
                print("2.Update")
                print("3.Delete")
                print("4.Display")
                print("5.Exiting")

                ch=int(input("Enter ur choice: "))


                if ch == 1:
                    Add()
                elif ch == 2:
                    Update()
                elif ch == 3:
                    Del()
                elif ch == 4:
                    Fetch()
                elif ch == 5:
                    print("Exit")
                    break
                else:
                    print("not a choice ")

        else:

            print("wrong input")


    c=input("Do u want to continue: ")


    def Add():
        px=int(input("how many data u want to enter: "))
        for i in range(1,px+1):

            x=int(input("Enter S_No: "))
            y=input("Enter E_no: ")
            z=input("Enter E_Name: ")
            a=input("Enter F_Name: ")
            b=input("Enter M_Name: ")
            c=input("Enter Address: ")
            d=input("Enter Age: ")
            e=input("Enter Department: ")
            f=input("Enter DOB: ")
            g=input("Enter DOJ: ")
            h=input("Enter Phone No: ")
            i=input("Enter Head: ")
            j=input("Enter Gender: ")
            k=input("Enter Pay: ")
            st="insert into emply(S_no,E_no,E_Name,F_Name,M_Name,Address,Age,depart,DOB,DOJ,P_no,head,Gender,pay)VALUES({},{},'{}','{}','{}','{}',{},'{}','{}','{}',{},'{}','{}',{})".format(x,y,z,a,b,c,d,e,f,g,h,i,j,k)
            cursor.execute(st)

            mycon.commit()
            print("record added")





    def Update():
        x=input("Change Employee Name? ")
        if x=='y':
            y=input("Enter Old Name: ")
            x=input("New name: ")
            t=("Update emply set E_Name='{}' where E_Name='{}'".format(x,y))
            cursor.execute(t)
            mycon.commit()


        y=input("Change Address? ")
        if y=='y':
            x=input("Old Address: ")
            y=input("New Address: ")
            z=input("employee name: ")
            tq=("Update emply set Address='{}' where Address='{}' AND E_Name='{}'".format(y,x,z))
            cursor.execute(tq)
            mycon.commit()


        z=input("Change Age? ")
        if z=='y':
            y=input("Old age: ")
            x=input("New age: ")
            z=input("employee name: ")
            tz=("Update emply set Age={} where Age={} AND E_Name='{}'".format(x,y,z))

