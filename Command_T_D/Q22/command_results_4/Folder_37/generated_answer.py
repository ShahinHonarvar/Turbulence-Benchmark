def find_sum_of_multiples(n):
    # create a list of first 17 multiples of the integer
    result = []
    for i in range(1, 18):
        # if the multiple is within the range of the integer, add it to the list
        if n <= i:
            result.append(n * i)
    # add all the elements in the list to find the sum
    return sum(result)
