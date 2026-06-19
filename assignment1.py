a=input("enter your name: ")
n=int(input("How many items do you want to buy? "))
list1=[]
totalBill=0
for i in range(n):
    itemname = input(f"Enter name of item number {i + 1}: ")
    itemprice=float(input(f"Enter price of item number {i+1}: "))
    list1.append(itemname)
    list1.append(itemprice)
    totalBill+=itemprice

totalAmount=totalBill

if totalBill>999:
    disc=0.2*totalBill
    totalBill-=disc
elif totalBill>499 and totalBill<1000:
    disc=0.1*totalBill
    totalBill-=disc
elif totalBill>199 and totalBill<500:
    disc=0.05*totalBill
    totalBill-=disc
else:
    disc=0

print("Customer name: "+a)
for i in range(0,2*n,2):
    print(list1[i])

print(f"Amount before discount is: {totalAmount}")
print(f"Total discount is: {disc}")
print(f"Total bill is: {totalBill}")

