
def sum_of_divisors_in_range(n):
    if n < 2:
        return 0

    divisors = []

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)

            if i * i <= n:
                j = i * i

                while j <= n:
                    if n % j == 0:
                        divisors.append(j)

                        j += i

                    else:
                        j += 1



    return sum(divisors)
