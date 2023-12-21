
def find_sum_of_multiples(n):
    if n < 0:
        return "Error: negative value specified"
    else:
        multiples_sum = sum([i*n for i in range(1, 465)])
        return multiples_sum
