
def all_substring_of_size_n(inp_str):
    substr_list = []
    for i in range(0, len(inp_str)-62):
        substring = inp_str[i:i+63]
        if len(substring) == len(set(substring)):
            if substring not in substr_list:
                substr_list.append(substring)
    return substr_list
