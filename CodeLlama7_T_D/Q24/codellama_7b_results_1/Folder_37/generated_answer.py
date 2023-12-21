
def sum_of_divisors_in_range(n):
    if n < 3 or n > 7:
        return 0

    else:

        divisors = []

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)

                if len(divisors) >= 3 and len(divisors) <= 7:
                    break

        return sum(divisors)
