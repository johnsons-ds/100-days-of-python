# prime = 2 % 2
# prime1 = 2 % 1


# print(prime, prime1)

n = int(input("Check this number: "))


def prime_checker(n):
    if n % n == 0 and n % 1 == 0:
        print("It's a prime number")
    else:
        print("It's not a prime number")


prime_checker(n)
