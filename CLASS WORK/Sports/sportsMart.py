class sportMart:
    def __init__(self):
        self.inventory = {}
        self.orders = {}

    def createInventory(self,ProductID,ProductName,Quantity,Price):
        temp = {
            "productid" : ProductID,
            "productname" : ProductName,
            "quantity" : Quantity,
            "price" : Price

        }

        self.inventory[ProductID]=temp

    def createOrder(self,OrderID,ProductID,Quantity,Price,Total):
         temp = {
              'orderid' : OrderID,
              'productid': ProductID,
              'quantity' : Quantity,
              'price': Price,
              'total' : Total
         }
         self.orders[OrderID] = temp
    
    def printOrders(self):
         print(self.orders)
    
    def printInventory(self):
         print(self.inventory)
    
trinity = sportMart()
orders = open("orders.csv","r")
o_header = orders.readline()
o_data = orders.readlines()
for data in o_data:
     tmp = data.strip().split(',')
     trinity.createOrder(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4])
trinity.printOrders()

#Create a menu driven program that will create new orders and update the inventory accordingly
#Export the final data to the field

lst=[]
def neworders(self,NewOID,NewPID,NewQuantity,NewPrice,NewTotal):
     temp = {
          'newid' : NewOID ,
          'newpid' : NewPID,
          'newquantity' : NewQuantity,
          'newprice' : NewPrice,
          'newtotal' : NewTotal

     }
     self.inventory[NewOID]=temp
     lst.append(temp())

     


      






    


