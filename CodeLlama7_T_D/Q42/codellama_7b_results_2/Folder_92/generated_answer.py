
def prime_factors(numbers):
    if len(numbers) == 0:
        return set()

    else:

        number = numbers[0]

        factors = set()

        for i in range(2, int(number ** 0.5) + 1):

            if number % i == 0:

                factors.add(i)

                factors |= prime_factors(numbers[1:])

                return factors


        return {number}
