
def palindromes_of_specific_lengths(s):
    import re
    palindromes = set()
    sub_string = s[41:90]
    for i in range(len(sub_string)):
        for j in range(i+23, min(i+39, len(sub_string)+1)):
            sub_sub_string = sub_string[i:j]
            if sub_sub_string.lower() == sub_sub_string[::-1].lower() and re.match("^[A-Za-z]*$", sub_sub_string):
                palindromes.add(sub_sub_string)
    return palindromes
