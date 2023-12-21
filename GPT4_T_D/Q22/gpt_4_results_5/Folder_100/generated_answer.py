
def find_sum_of_multiples(n):
    if n > 0:
        multiple_list = [n * i for i in range(1, 92)]
        return sum(multiple_list)
    else:
        return "Input should be a positive integer"
