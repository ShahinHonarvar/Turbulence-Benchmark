 def find_sum_of_multiples(num):
    sum = 0
    for i in range(1, 187):
        if num * i > 0:
            sum += num * i

    return sum
