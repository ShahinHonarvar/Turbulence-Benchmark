
def all_substring_of_size_n(input_string):
    if len(input_string) < 48:
        return []
    else:
        substrings = []
        for i in range(len(input_string) - 47):
            substring = input_string[i:i+48]
            if len(set(substring)) == len(substring):
                if substring not in substrings:
                    substrings.append(substring)
        return substrings
