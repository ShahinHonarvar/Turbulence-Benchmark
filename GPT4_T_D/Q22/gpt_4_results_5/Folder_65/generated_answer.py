
def find_sum_of_multiples(n):
    if n <= 0:
        return "Please provide a positive integer"
    else:
        sum = 0
        for i in range(1, 81):
            sum += i * n
        return sum 
