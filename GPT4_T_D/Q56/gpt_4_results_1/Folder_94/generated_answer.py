
def all_substring_of_size_n(input_string):
    substring_list = []
    for i in range(len(input_string) - 69):
        substring = input_string[i:i+70]
        if len(set(substring)) == len(substring):
            if substring not in substring_list:
                substring_list.append(substring)
    return substring_list
