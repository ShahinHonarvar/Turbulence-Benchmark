
def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string) - 77):
        substring = input_string[i : i + 78]
        if len(set(substring)) == len(substring):
            substrings.append(substring)
    return list(set(substrings))
