
def return_binary_or_hexa(tuple):
    # Initialize variables
    a = tuple[50]
    b = tuple[200]
    sum = 0
    binary_repr = ''
    hexa_repr = ''

    # Calculate the sum of all integers from a + 1 to b - 1 (both inclusive) that are not present in the tuple between indices 50 and 200
    for i in range(a + 1, b):
        if i not in tuple[50:200]:
            sum += i

    # Convert the sum to binary representation and return it

    if sum % 2 == 0:
        binary_repr = format(sum, 'b')

        return binary_repr.lstrip('0')

    else:
        hexa_repr = format(sum, 'x')

        return hexa_repr.lower().lstrip('0')
