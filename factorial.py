from re import I

n = int(input("write a number to calculate it's factorial\n"))

fact = 1   
i = 1

while i<= n:
    fact = fact * i
    i += 1

print(fact)