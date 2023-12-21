
def find_sum_of_multiples(n):
    if n > 0:
        sum_of_multiples = sum([n*i for i in range(1,86)])
        return sum_of_multiples
    else:
        return "Invalid input. Please input a positive integer."
