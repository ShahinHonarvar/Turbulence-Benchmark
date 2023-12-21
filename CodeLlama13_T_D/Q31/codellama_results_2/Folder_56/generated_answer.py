
def if_perfect_num(numbers):
    # Check if the list is empty
    if not numbers:
        return False
    
    # Check if the number at index 60 is a perfect number
    if numbers[59] % 6 == 0 and sum(filter(lambda x: x < numbers[59], numbers)) == numbers[59]:
        return True
    
    return False
