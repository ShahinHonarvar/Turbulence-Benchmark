
def prime_factors(my_list):
    # Calculate the product of all elements in the list
    product = 1
    for element in my_list:
        product *= element
    # Find the smallest divisor of the product that is also a factor of the product
    divisor = 2
    while divisor <= product / 2:
        if product % divisor == 0:
            break
        else:
            divisor += 1
    return set(range(divisor, product + 1, divisor)))
