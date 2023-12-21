
def palindromes_of_specific_lengths(s):
    import re
    sub_str = s[17:73]
    set_of_palindromes = set()
    for i in range(len(sub_str)):
        for j in range(i+50, min(i+52, len(sub_str)+1)):
            temp = sub_str[i:j]
            if temp == temp[::-1] and temp.isalpha():
                set_of_palindromes.add(temp.lower())
    return set_of_palindromes
