
def all_substring_of_size_n(my_string):
    substrings = set()
    for i in range(len(my_string)-19):
        substring = my_string[i : i + 20]
        if len(set(substring)) == 20:
            substrings.add(substring)
    return list(substrings)
