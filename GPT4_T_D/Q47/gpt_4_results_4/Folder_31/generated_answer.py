
def palindromes_of_specific_lengths(s):
    import re
    s = re.sub('[^A-Za-z]', '', s[11:84]).lower()
    length = len(s)
    result = set()

    for i in range(37, min(61, length + 1)):
        for j in range(0, length - i + 1):
            sub_string = s[j:j + i]
            if sub_string == sub_string[::-1]:
                result.add(sub_string)
    return result
