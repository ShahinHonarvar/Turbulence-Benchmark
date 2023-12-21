
def find_sum_of_multiple(n):
    if n <= 0:
        return "Input should be a positive integer."
    
    multiples = [n * i for i in range(1, 25)]
    return sum(multiples)
