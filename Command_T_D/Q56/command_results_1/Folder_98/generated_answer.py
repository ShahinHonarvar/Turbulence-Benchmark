def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 9):
        for j in range(i + 1, len(s) - 8):
            if s[i:j + 10] not in result:
                result.append(s[i:j + 10])
    return result
