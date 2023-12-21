def all_substring_of_size_n(str):
    return [sub for sub in set(str[i:i + 89]) if len(set(sub)) == 89]
