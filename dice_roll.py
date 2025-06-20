import random
list1 = [1, 2, 3, 4, 5, 6]
inp = int(input("roll:0/exit:1 :"))
while inp == 0:
    print(random.choice(list1))
    print(random.choice(list1))
    inp = int(input("roll:0/exit:1 :"))
print("--thankyou for playing!!!--")
