count=0
total=0

family=[]
while count <=5:
    name=input("enter your name: ")
    age=int(input("enter your age: "))
    family_member={}
    family_member['name']=name
    family_member['age']=age
    family.append(family_member)
    count+=1
    print(family)

    if count ==5:
        for i in family:
            print(f"{i['name']} is {i['age']}")
            total+=i['age']
            average=total/count
        print(f"The total of the family's ages is {total}")
        print(f"The average of the ages is {average}")
        if average >60:
            print("The family is old.")
        else:
            print("The family is young")

        break


