class Product:
    def __init__(self,name,num,price):
        self.name=name
        self.price=price
        self.num=num

def discount(prod_tot):
    if prod_tot >=6000:
       discount=0.05 * prod_tot
    elif (prod_tot>3000) and (prod_tot<=5900):
        discount=0.03* prod_tot
    else:
        discount=0
    return discount
    

count=0
total=0
prod_list=[]
while count <=4:
    prod_name=input("enter name of product: ")
    prod_num=int(input("enter product number: "))
    prid_price=int(input("enter price: "))
    new_product=Product(name=prod_name,num=prod_num,price=prid_price)
    prod_list.append(new_product.price)
    print(prod_list)
    count+=1
    if count == 4:
        print("finished!")
        for i in prod_list:
            total+=i
        print(f"The total is {total}")
        print(f"The discount is {discount(total)}")
        gross_total=total-discount(total)
        print(f"The net total is {gross_total}")
        break

