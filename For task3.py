from math import gcd


number = 20
for x in range(21):
    if number <= 20:
        total = number - x
        print(total)

for x in range(1, 21):
    if x % 2 == 0:
        print(x)

for x in range(1, 6):
    total = x * "*"
    print(total)

a = 66
b = 90
total = gcd(a , b)
print(f" The GCD is {total}")
