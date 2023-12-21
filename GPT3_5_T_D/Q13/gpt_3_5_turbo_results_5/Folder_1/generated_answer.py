
def find_second_largest_num(numbers):
    extracted_numbers = numbers[31:73]
    if len(extracted_numbers) <= 1:
        return None
    extracted_numbers.sort()
    return extracted_numbers[-2]
