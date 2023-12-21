def palindromes_of_specific_lengths(str):
    str = str[40:90]
    str = str.lower()
    pal = set()
    for x in range(23, 39):
        i = str.find(str[x:x + 2], 1)
        while i != -1:
            j = str.find(str[x:x + 2], i + 1)
            if j == -1:
                break
            if str[i:j] == str[i][::-1]:
                pal.add(str[i:j])
            i = str.find(str[x:x + 2], j + 1)
    return pal
