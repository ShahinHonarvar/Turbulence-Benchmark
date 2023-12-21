def find_sum_of_multiples(n):
    # find_sum_of_multiples function
    # Take n as an argument and return the sum of the first 99 multiples of n
    # Function should not contain any comments
    # Function delimited by triple backticks
    # n = positive integer
    # return = sum of the first 99 multiples of n
    a = 1
    b = n * 100
    result = 0
    while a <= b:
        result += a
        a += n
    return result
