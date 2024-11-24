import random
#print(dir(random))
#you can also go and check the implementation

lb =int(input("Please enter lower bound: "))
ub=int(input("Please enter upper bound: "))
print(random.randint(lb+1,ub-1))