 def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[3]
    b = tuple_of_integers[9]
    sum_of_integers = 0

    for i in range(a + 1, b):
        if i not in tuple_of_integers:
            sum_of_integers += i

    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]

    else:

        return hex(sum_of_integers)[2:].upper()
