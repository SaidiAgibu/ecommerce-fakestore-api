import csv
import json
import requests
import pandas as pd 

def register():
    try:
        with open('main.csv','a', newline="") as file:
            filednames = ['name','email','password']
            writer = csv.DictWriter(file, filednames)
            writer.writeheader()
            writer.writerow({'name':input("enter your name:") ,
                            'email':input("enter your email:") ,
                            'password':input("enter your password:")})
            print("you have successfully created an account")
    except Exception as Error:
        print(Error)

   


def login():
    try:
        with open('main.csv','r') as file:
            email = input("enter your email:")
            password = input("enter your password:")
            reader = csv.reader(file)
            for row in reader:
                if email and password in row:
                    print("you have successfully logged in")
        
    except Exception as Error:
        print(Error)

def view_product():
    try:
        file = open('products.json')
        data = json.load(file)
        for i in data['products']:
            i = json.dumps(i, indent=4)
            print(i)
        file.close()
                
    except Exception as Error:
        print(Error)




#trying to get produts from an api 
def getData():
    try:
        url = 'https://fakestoreapi.com/products'
        results = requests.get(url).json()
        data_found = json.dumps(results, indent=4)

        #storing the data inside products json file
        with open('products.json', 'w') as data:
            data.write(data_found)
            print("data taken successfully from the api")
    except Exception as Error:
        print(Error)



def main():
    while True:
        print(">>>>>>>>SAIDI ECOMMERCE<<<<<<<<<")
        choice = int(input("1.Register\n2.View Products\n3.My Account\n WHAT DO YOU WANT TO DO:"))
        if choice == 1:
            print(">>>>>>REGISTER PAGE<<<<<<<")
            register()
            print(">>>>>>LOGIN PAGE<<<<<<<")
            login()
            c = input("do you want to continue or exit (y/n):")
            if c == 'y':
                continue
            else:
                print("thank you for using our shop")
                break
        elif choice == 2:
            print(">>>>>>VIEW PRODUCTS<<<<<<<")
            view_product()
            c = input("do you want to continue or exit (y/n):")
            if c == 'y':
                continue
            else:
                print("thank you for using our shop")
                break
    
        
        
main()