
def find_sum_of_multiple(n):
    if n > 0:
        return sum([i*n for i in range(1, 57)])
    else:
        return "Invalid input. Please enter a positive integer."
