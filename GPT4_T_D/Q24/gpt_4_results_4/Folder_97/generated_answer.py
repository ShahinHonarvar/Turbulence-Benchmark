
def sum_of_divisors_in_range(number):
    s = 0
    for i in range(615, 793):
        if number % i == 0:
            s += i
    return s
