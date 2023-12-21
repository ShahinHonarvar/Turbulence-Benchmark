
def all_substring_of_size_n(input_str):
    substring_set = set()
    for i in range(len(input_str)):
        if len(input_str[i:i+34]) == 34 and len(set(input_str[i:i+34])) == 34:
            substring_set.add(input_str[i:i+34])
    return list(substring_set)
