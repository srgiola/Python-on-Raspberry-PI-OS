import pyrebase
import os

os.system('clear')

firebaseConfig = {
    "apiKey": "AIzaSyDpsyWxcFCv0YEbAHNgrqzyVat-Wx4WQlo",
    "authDomain": "bdsergiopi.firebaseapp.com",
    "databaseURL": "https://bdsergiopi-default-rtdb.firebaseio.com",
    "projectId": "bdsergiopi",
    "storageBucket": "bdsergiopi.appspot.com",
    "messagingSenderId": "34942479441",
    "appId": "1:34942479441:web:24bd6daea39d7f2d3a1c70",
    "measurementId": "G-09DEEP35PH"
    }

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

print("Conexion realizada")

db.set({})
print("set enviado")

#Push with Firebase key
#data = {"name":"John", "age":20, "addres":["New York", "Los Angeles"] }
#db.push(data)

#Push with my own key
#db.child("Doe").set(data)

data = {"name":"John", "age":20, "addres":["New York", "Los Angeles"] }
db.child("Branch Push").child("Employee").push(data)
print("push enviado")

data = {"name":"Susana", "age":19, "addres":["London", "Wesex"] }
db.child("Branch Push").child("Employee").child("Lara").set(data)
print("set enviado")

#Update
data = {"name":"John", "age":20, "addres":["New York", "Los Angeles"] }
db.child("Branch Update").child("Employee").push(data)
print("push enviado")

data = {"name":"Susana", "age":19, "addres":["London", "Wesex"] }
db.child("Branch Update").child("Employee").child("Lara").set(data)
print("set enviado")

data = {"name":"Evelyn", "age":19, "addres":["London", "Wesex"] }
db.child("Branch Update").child("Employee").child("Vasquez").set(data)
print("set enviado")

db.child("Branch Update").child("Employee").child("Lara").update({"name":"Sergio"})
print("Update Enviado")

data = {"Branch Update/Employee/Vasquez":{"name":"Yani", "age":50, "addres":["Paris", "Chatou"]}}
db.update(data)
print("Update Enviado")

registros = db.child("Branch Update").child("Employee").get()
for registro in registros.each():
    print(registro.val())
    print(registro.key())
    if(registro.val()['name'] == "John"):
        key = registro.key()
        db.child("Branch Update").child("Employee").child(key).update({"addres":["New Jersey", "Oklahoma"]})
        print("Update Enviado")

#Delete
data = {"name":"Susana", "age":19, "addres":["London", "Wesex"] }
db.child("Branch Delete").child("Employee").child("Lara").set(data)
print("set enviado")

data = {"name":"Evelyn", "age":19, "addres":["London", "Wesex"] }
db.child("Branch Delete").child("Employee").child("Vasquez").set(data)
print("set enviado")

db.child("Branch Delete").child("Employee").child("Lara").remove()
print("Delete Enviado")


