
def find_sum_of_multiples(num):
    return sum(range(1, 97) if i % num == 0 else 0 for i in range(1, 97))
