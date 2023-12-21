
def find_sum_of_multiple(n):
    if n <= 0:
        return "Number must be a positive integer"
    else:
        return sum(n * i for i in range(1, 187))
