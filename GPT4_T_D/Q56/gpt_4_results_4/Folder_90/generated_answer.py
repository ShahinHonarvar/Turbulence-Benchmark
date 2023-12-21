
def all_substring_of_size_n(input_string):
    if len(input_string) < 130:
        return []
    distinct_substrings = set()
    for i in range(len(input_string) - 129):
        substring = input_string[i:i+130]
        if len(set(substring)) == 130:
            distinct_substrings.add(substring)
    return list(distinct_substrings)
