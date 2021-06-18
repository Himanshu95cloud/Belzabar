import math
from time import perf_counter


# # There are additional bonus points for elegance,
# adequate code comments describing the algorithm(s) used, focus on coding conventions, optimal speed and time complexity and readability.

class Sol:
    """# Belzabar is 19 years old. On this occasion, we formulated the Belzabar Number.
#  A positive integer is a Belzabar number if it can be represented either as (n * (n + 19)) OR (n * (n - 19)),
# where n is a prime number."""

    def __init__(self):
        self.prime = None
        self.belz = []
        self.belz_count = 0

    def primeNums(self, n):
        primes = []

        self.prime = [True for i in range(n + 1)]

        p = 2
        while (p * p <= n):
            if self.prime[p] == True:
                # Update all multiples of p
                for i in range(p * p, n + 1, p):
                    self.prime[i] = False
            p += 1

        # Print all prime numbers
        for p in range(2, n + 1):
            if self.prime[p]:
                primes.append(p)

        self.prime = primes
        return len(primes)

    # # Write a function named 'is_belzabar_number' which accepts a number as input and determines
    # if it is a Belzabar Number (or not). Input to the function will be a number and the output will be boolean.
    # # For bonus points,
    # # 1. Write a function that calculates and prints the count of Belzabar numbers less than or equal to 1 million(10 Lacs).
    # # 2. Write a function that calculates and prints the count of Belzabar numbers from bonus question #1 above that are prime.

    def total_belzabar_number(self, num):
        for i in range(2, num + 1):
            if self.check_belz(i):
                self.belz_count += 1
                self.belz.append(i)

        return self.belz_count

    def check_belz(self, num):
        self.primeNums(num)
        p = self.prime
        if num < 0:
            return False
        for N in p:
            if (N * (N + 19)) == num or (N * (N - 19)) == num:
                return True
        return False


if __name__ == "__main__":
    start = perf_counter()
    num = int(input("Enter a number : "))
    obj = Sol()
    print("Input number is Belzabar or not?")
    print(obj.check_belz(num))
    print("total prime numbers are within {} are:".format(num))
    print(len(obj.prime))
    print("Total Belzabar numbers are within {} are: ".format(num))
    print(obj.total_belzabar_number(num))
    print("Belzabar numbers are: ")
    print(obj.belz)

    end = perf_counter()
    print("time taken: ", end - start)
