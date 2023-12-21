
def return_binary_or_hexa(numbers):
    a = numbers[80]
    b = numbers[200]
     # set up a set of numbers that between a+1 to b-1 both inclusive
    complete_set = set(range(a+1, b))
    # slice out numbers between a and b from the tuple and convert into set
    subset = set(numbers[80:201])
    # find out those numbers that are not in the subset
    missing_set = complete_set - subset

    sum_missing = sum(missing_set)
    # if no missing numbers
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()
