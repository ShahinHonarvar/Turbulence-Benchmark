
def find_largest_num(numbers):
    if len(numbers) > 111:
        return max(numbers[111:112])
    else:
        return 'List is not long enough'
