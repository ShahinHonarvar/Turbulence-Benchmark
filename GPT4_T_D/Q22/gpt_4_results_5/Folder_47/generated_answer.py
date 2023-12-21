
def find_sum_of_multiples(n):
    assert n > 0, 'The input should be a positive integer'
    return n * sum(range(1, 39))
