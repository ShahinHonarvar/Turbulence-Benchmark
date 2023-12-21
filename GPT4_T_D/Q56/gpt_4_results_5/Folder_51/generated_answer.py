
def all_substring_of_size_n(original_str):
    substr_list = list()
    for i in range(len(original_str)):
        if len(original_str[i:i+96]) == 96:
            if len(set(original_str[i:i+96])) == 96:
                if original_str[i:i+96] not in substr_list:
                    substr_list.append(original_str[i:i+96])
    return substr_list
