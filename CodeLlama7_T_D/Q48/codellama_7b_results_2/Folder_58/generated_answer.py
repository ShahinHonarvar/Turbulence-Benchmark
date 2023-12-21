
def return_binary_or_hexa(my_tuple):
    a = my_tuple[275]
    b = my_tuple[871]
    sum = 0
    for i in range(a + 1, b - 1):
        if i not in my_tuple[275:871]:
            sum += i

    if sum % 2 == 0:
        return f"{sum:x}"

    else:

        return f"{sum:b}"
