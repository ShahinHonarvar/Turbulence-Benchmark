def all_substring_of_size_n(s):
    return [
        s[i:i + 21]
        for i in range(0, len(s) - 20)
    ]
