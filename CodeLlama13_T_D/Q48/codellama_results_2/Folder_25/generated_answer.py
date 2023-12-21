
def return_binary_or_hexa(tuple_of_distinct_nonnegative_integers):
    a = tuple_of_distinct_nonnegative_integers[37]
    b = tuple_of_distinct_nonnegative_integers[43]

    sum_of_integers = 0
    for i in range(a+1, b):
        if i not in tuple_of_distinct_nonnegative_integers:
            sum_of_integers += i

    if sum_of_integers % 2 == 0:
        return format(sum_of_integers, 'x')
    else:
        return bin(sum_of_integers)[2:]
