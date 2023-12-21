def return_n_smallest_chars(str_list):
    result = []
    for char in str_list:
        if char not in result:
            result.append(char)
            if len(result) == 11:
                break
    result.sort(key=lambda x: ord(x))
    return result
