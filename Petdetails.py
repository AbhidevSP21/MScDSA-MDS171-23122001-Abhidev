#Create a petstore class where you have the details of pets available and their details'user 
#The class will have methods
#Store a new pet details
#Search for a pet
#List all pets

#Importing your petstore class,create a petstoremain file,where you will implement a menu driven program for admin - who will manage the store and user who will see the pets and buy pets

class pets:

    def _init_(self):
       
        self.petlist =  [
            {
            'Category' : 'dog',
            'Price' : '500' ,
            'Age' : '2' ,
            'status':'unsold',
        },
        {
            'Category' : 'cat',
            'Price' : '700' ,
            'Age' : '1' ,
            'status':'unsold',

        },
        {
            'Category' : 'parrot',
            'Price' : '50' ,
            'Age' : '4' ,
            'status':'unsold'
        }

        ]

    def storeNewpets(self):
        n=int(input("enter the number of pets to be added"))
        
        for i in range(n):
            pet=input("enter the pet")
            price=int(input("enter thr price"))
            age=int(input("enter he age"))
            status=input("Enter whether sold")
            store={"category":pet,"price":price,"age":age,"status":status}
        self.petlist.append(store)
            
        print(self.petlist)

    def searchPets(self):
        enter=input("enter the name to be searched")
        for pet  in self.petlist:
            
            if enter.strip().lower() in pet.values():
                print(pet.values())
                break
            else:
                print("no pets found")

    def sellPets(self):
        sell=input("enter the pet you want to sell")
        for i in self.petlist:
            if sell in i.values():
                i['status']:"sold"
                print(self.petlist)
                break
    
    def listPets(self):
        for pets in self.petlist:
            print(pets.values())