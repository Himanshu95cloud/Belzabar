import math
from time import perf_counter


# # There are additional bonus points for elegance,
# adequate code comments describing the algorithm(s) used, focus on coding conventions, optimal speed and time complexity and readability.

class Sol:
    """# Belzabar is 19 years old. On this occasion, we formulated the Belzabar Number.
#  A positive integer is a Belzabar number if it can be represented either as (n * (n + 19)) OR (n * (n - 19)),
# where n is a prime number."""

    def isPrime2(self, n):
        if n == 1:
            return False

        for i in range(2, int((n) ** (1 / 2)) + 1):
            if n % i == 0:
                return False
        return True

    def nextPrime(self, N):
        if (N <= 1):
            return 2

        prime = N
        found = False

        while (not found):
            prime = prime + 1

            if (self.isPrime2(prime) == True):
                found = True

        return prime

    # # Write a function named 'is_belzabar_number' which accepts a number as input and determines
    # if it is a Belzabar Number (or not). Input to the function will be a number and the output will be boolean.
    # # For bonus points,
    # # 1. Write a function that calculates and prints the count of Belzabar numbers less than or equal to 1 million(10 Lacs).
    # # 2. Write a function that calculates and prints the count of Belzabar numbers from bonus question #1 above that are prime.
    def is_belzabar_number(self, num):
        # num is prime
        sieve = []

        if num < 0:
            return False
        else:
            N = 2
            while N < num:
                print("executing greater than for N =", N)
                if (N * (N + 19)) == num:
                    sieve.append(N)
                else:
                    N = self.nextPrime(N)

            N = 19
            while N < num:
                print("executing less than for N =", N)
                if N < 19:
                    return False
                elif (N * (N - 19)) == num:
                    sieve.append(N)
                    N = self.nextPrime(N)
                else:
                    N = self.nextPrime(N)
        return sieve


if __name__ == "__main__":
    start = perf_counter()
    num = int(input("Enter a number : "))
    obj = Sol()
    result = obj.is_belzabar_number(num)
    print(result)
    end = perf_counter()
    print("time take: ", end - start)
