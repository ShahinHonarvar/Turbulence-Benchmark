
def find_sum_of_multiples(n):
    if isinstance(n,int) and n>0:
        return sum([i*n for i in range(1, 417)])
    else:
        return "Input must be a positive integer"
