
def find_second_smallest_num(numbers):
    if len(numbers) <= 200:
        return None
    else:
        sorted_numbers = sorted(numbers[70:201])
        second_smallest = sorted_numbers[1]
        return second_smallest
