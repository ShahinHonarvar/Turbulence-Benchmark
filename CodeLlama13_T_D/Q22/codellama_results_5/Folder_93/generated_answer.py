
def find_sum_of_multiples(integer):
    return sum([i for i in range(1, 67) if i % integer == 0])
