
def find_sum_of_multiples(n):
    if n <= 0:
        return "Please enter a positive integer"
    else:
        sum = 0
        for i in range(1, 207):
            sum += n*i
        return sum
