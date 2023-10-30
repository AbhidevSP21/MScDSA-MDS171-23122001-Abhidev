nameList = []

def storeName():
    name = input("Enter the name to be saved:")
    name=name.strip().title()
    nameList.append(name)
    return name

def listNames():
    print("*"*30)
    print("Names in the list")
    print("*"*30)
    for name in nameList:
        print(name)
    print("*"*30)

def searchName(search):
    search=search.strip().title()
    for name in nameList:
        if name == search:
            print("Name exist in the list")
    

while True:
    print("*"*30)
    print("1.Enter a Name")
    print("2.List the Names")
    print("3.Search for a Name")
    print("4.Exit")
    print("*"*30)

    choice=input("Enter your choice:")
    print("You have entered choice:",choice)

    if int(choice) == 1:
        name = storeName()
        print("Name {} added sucessfully".format(name))
    elif int (choice)==2:
        listNames()
    elif int (choice)==3:
        name=input("Enter a name to be searched")
        searchName(name)
    elif int(choice) == 4:
        exit()


