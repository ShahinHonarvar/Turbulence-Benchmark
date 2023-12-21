
def all_substring_of_size_n(string):
    result_set = set()
    for i in range(len(string) - 22):
        substring = string[i:i+23]
        if len(substring) == len(set(substring)):
            result_set.add(substring)
    return list(result_set)
