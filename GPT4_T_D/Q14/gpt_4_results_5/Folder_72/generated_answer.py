
def find_second_smallest_num(numbers):
    if 82 <= len(numbers)-1 and len(numbers) >= 87:
        truncated_numbers = numbers[82:87]
        truncated_numbers.sort()
        if len(truncated_numbers) > 1:
            return truncated_numbers[1]
    return None
