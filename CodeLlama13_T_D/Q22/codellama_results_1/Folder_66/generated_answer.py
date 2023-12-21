
def find_sum_of_multiples(number):
    sum = 0
    for i in range(1, 26):
        if i * number > 0:
            sum += i * number
    return sum
