# class expenseTracker:
#     def _init_(self):
#         self.transactionDetails={"details":[]}

#     def retrieveTransactions(self):
#         for i in open("Expense_Income_Tracker.csv","r+").readlines():
#             line=i.split(",")
#             if line[1]!="Expense Category":
#                 transaction={"type":line[0],"category":line[1],"amount":line[2],"description":line[3],"date":line[4]}
#                 self.transactionDetails["details"].append(transaction)

#     def calculateTotal(self):
#         totalIncome=0
#         totalExpense=0
#         for i in self.transactionDetails["details"]:
#             if i["type"]=="Income":
#                 totalIncome+=int(i["amount"])
#             else:
#                 totalExpense+=int(i["amount"])
#         return totalIncome,totalExpense
    
#     def addTransaction(self,type,category,amount,description,date):
#         transaction={"type":type,"category":category,"amount":amount,"description":description,"date":date}
#         self.transactionDetails["details"].append(transaction)
    
#     def writeTransactions(self):
#         file=open("Expense_Income_Tracker.csv","w+")
#         file.write("Type,Expense Category,Amount,Description,Date\n")
#         for i in self.transactionDetails["details"]:
#             date=str(i["date"]).strip()
#             file.write(i["type"]+","+i["category"]+","+i["amount"]+","+i["description"]+","+date+"\n")
#         file.close()


# order=expenseTracker()
# order.retrieveTransactions()
# while True:
#     print("1.Add New Transaction\n2.Calculate Total Income and Expense\n3.Exit")
#     choice=int(input("Select your action:"))
#     if choice==1:
#         type=input("Enter the type of transaction (Income/Expense):")
#         category=input("Enter the category:")
#         amount=input("Enter the amount:")
#         description=input("Enter the description of transaction:")
#         date=input("Enter the date mm/dd/yyyy:")
#         order.addTransaction(type,category,amount,description,date)
#     elif choice==2:
#         totalIncome,totalExpense=order.calculateTotal()
#         print("Total Income=",totalIncome,"\nTotal Expense=",totalExpense)
#         order.writeTransactions()
#     elif choice==3:
#         order.writeTransactions()
#         exit()
import random
class sportmart:
    def __init__(self):
        self.inventory={}
        self.orders={}

    def  createorder(self,Orderid,ItemName,Quantity,Price,Total):
        temp={"orderid":Orderid,
              "itemname":ItemName,
              "quantity":Quantity,
              "price":Price,
              "total":Total
              }
        
        self.orders[Orderid]=temp
        return temp

    def createinventory(self,ProductID,ProductName,Quantity,Price):
        temp={"productid":ProductID,
             "productname":ProductName,
             "quantity":Quantity,
             "price":Price
             }
        self.inventory[ProductID]=temp
    
    def printorders(self):
        print("\n",self.orders)

    def printinventory(self):
        print(self.inventory)

    def generateid(self):
        first="OD"
        orderid=''
        for i in range(1,4,1):
            orderid+=str(random.randint(i,9))
        orderid=first+orderid
        return orderid
    
    def updateinventory(self,name,qty):
        for item in self.inventory.values():
            if item['productname']==name:
                item['quantity']=int(item['quantity'])-qty
        print("\nThe updated inventory data:\n")
        self.printinventory()

    def storefile(self):
        file=open("newdata.csv","a+")
        file.write(str(self.inventory))
        file.close()

trinity=sportmart()


while True:
    print("\nMenu Driven Program\n")
    print("1. Print Orders\n2. Print Inventory\n3. Export Data")
    choice=int(input("Enter your choice:"))
    if choice==1:
        orders=open("Order.csv","r")
        orders_header=orders.readline()
        orders_orders=orders.readlines()
        for item in orders_orders:
            temp=item.strip().split(',')
            trinity.createorder(temp[0],temp[1],temp[2],temp[3],temp[4])
        trinity.printorders()
    
    elif choice==2:
        inventory=open("Inventory.csv","r")
        inventory_header=inventory.readline()
        inventory_list=inventory.readlines()
        for item in inventory_list:
            temp=item.strip().split(',')
            trinity.createinventory(temp[0],temp[1],temp[2],temp[3])
        trinity.printinventory()

    elif choice==3:
        add={}
        itemname=input("Enter item name:").title()
        quantity=int(input("Enter quantity:"))
        price=int(input("Enter price:"))
        total=price*quantity
        id=trinity.generateid()
        #add=trinity.createorder(id,itemname,quantity,price,total)
        trinity.orders[id] = trinity.createorder(id,itemname,quantity,price,total)
        trinity.printorders()
        print("\n\n")
        trinity.updateinventory(itemname,quantity)
    elif choice==4:
        trinity.storefile()
    elif choice==5:
        exit()
    else:
        print("Wrong choice")