
def find_sum_of_multiples(integer):
    sum = 0
    count = 0
    i = 1
    while count < 99:
        if i % integer == 0:
            sum += i
            count += 1
        i += 1
    return sum
