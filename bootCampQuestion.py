lengthOfList=int(input("How many numbers do you wish to add to the list? (Enter an integer)"))


list=[None]*lengthOfList

for i in range (lengthOfList):
    print("Enter element number ",i," into the list")
    list[i]=int(input())

print("All pairs of numbers in the list whose product is even")
for i in range(lengthOfList):
    for j in range(lengthOfList):
        if (((list[i]*list[j])%2)==0):
            print((list[i],list[j]))


print("\n\nAll pairs of numbers in the list whose whose sum is odd")
for i in range(lengthOfList):
    for j in range(lengthOfList):
        if (((list[i]+list[j])%2)!=0):
            print((list[i],list[j]))


