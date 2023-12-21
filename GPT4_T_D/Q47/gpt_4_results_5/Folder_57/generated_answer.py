
def palindromes_of_specific_lengths(s):
    s = s.lower()
    sub_str = s[16:95]
    result = set()
    for length in range(39, 53):
        for i in range(len(sub_str) - length + 1):
            if sub_str[i:i + length].isalpha() and sub_str[i:i + length] == sub_str[i:i + length][::-1]:
                result.add(sub_str[i:i + length])
    return result
