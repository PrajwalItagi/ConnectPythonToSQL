# importing pyodbc library
import pyodbc

# all the credentials required to connect to the database
server = 'Your_Server_Name'
database = 'Your_Database_Name'
username = 'Your_Username@Your_Server_Nmae'
password = 'Your_Password'
driver = '{ODBC Driver 17 for SQL Server}'
port = 'Your_Port'

#Connection String
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT='+port+';DATABASE='+database+';UID='+username+';PWD='+password)
mycursor = cnxn.cursor()

#Inserts data into the table
mycursor.execute("INSERT INTO Users(UserID, EmailID, Password, PhoneNumber, City, Country) VALUES (?,?,?,?,?,?)",('Arvind','arvind.itagi@gmail.com','arvind123','9845211787','Banglore','India'))


#Deletes data whose UserID is 'Arvind'
mycursor.execute("DELETE FROM Users where UserID='Arvind'")

cnxn.commit()

mycursor.execute("SELECT * FROM Users")

#Prints the table
 for row in mycursor:
     print(row)
