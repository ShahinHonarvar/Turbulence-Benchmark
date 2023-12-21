
def find_second_largest_num(numbers):
    numbers = numbers[100:201] # Extract sublist from index 100 to 200
    numbers.sort() # Sort the sublist in ascending order
    if len(numbers) < 2: # Check if there are at least two elements
        return None
    else:
        return numbers[-2] # Return the second largest element
