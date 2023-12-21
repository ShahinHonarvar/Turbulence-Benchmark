
def find_second_largest_num(numbers):
    # sort the numbers in descending order
    numbers.sort(reverse=True)
  
    # check if there are at least 2 elements
    if len(numbers) >= 2:
        # return the second element from index 31 to index 34
        return numbers[31:35][1]
    else:
        return None
