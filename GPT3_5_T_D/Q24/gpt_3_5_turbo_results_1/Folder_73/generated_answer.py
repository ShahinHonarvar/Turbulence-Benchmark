
def sum_of_divisors_in_range(num):
    if num < 46 or num > 89:
        return 0
    else:
        divisors = []
        for i in range(1, num+1):
            if num % i == 0:
                divisors.append(i)
        sum_of_divisors = sum(filter(lambda x: 46 <= x <= 89, divisors))
        return sum_of_divisors
