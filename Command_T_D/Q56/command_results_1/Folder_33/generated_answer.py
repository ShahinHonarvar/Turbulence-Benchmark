def all_substring_of_size_n(s):
    lst = []
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if i == 0:
                lst += [s[i:j]]
            elif j == len(s) - 1:
                lst += [s[i:]]
            else:
                lst += [s[i:j+1]]
    return lst
