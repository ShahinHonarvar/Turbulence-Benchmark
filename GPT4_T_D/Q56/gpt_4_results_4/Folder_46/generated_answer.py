
def all_substring_of_size_n(input_string):
    substring_set = set()
    length = len(input_string)
    for i in range(length):
        if i + 87 <= length:
            substring = input_string[i:i+87]
            if len(set(substring)) == len(substring):
                substring_set.add(substring)
    return list(substring_set)
