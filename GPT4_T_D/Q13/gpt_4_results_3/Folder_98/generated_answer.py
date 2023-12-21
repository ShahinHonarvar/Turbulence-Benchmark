
def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    else:
        return sorted(numbers[:7], reverse=True)[1]
