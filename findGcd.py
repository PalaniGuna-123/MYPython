def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(54, 24)) 


def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

print(gcd(2,6))
