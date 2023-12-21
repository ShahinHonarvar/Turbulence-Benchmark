
def find_second_largest_num(numbers):
    if len(numbers) < 55:
        return None
    else:
        return sorted(numbers[50:55], reverse=True)[1]
