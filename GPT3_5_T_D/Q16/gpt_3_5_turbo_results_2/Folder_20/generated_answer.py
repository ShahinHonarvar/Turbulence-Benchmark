
def sum_even_ints_inclusive(numbers):
    even_sum = 0
    
    for index in range(56, 67):
        if index < len(numbers) and numbers[index] % 2 == 0:
            even_sum += numbers[index]
    
    return even_sum
