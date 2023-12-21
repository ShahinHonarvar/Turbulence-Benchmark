
def find_sum_of_multiples(n):
    if n > 0:
        return sum(n * i for i in range(1, 78))
    else:
        return "Input should be a positive integer"
