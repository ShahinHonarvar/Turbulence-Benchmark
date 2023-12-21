
def palindromes_of_specific_lengths(s):
    import re
    sub_string = s[10:75]
    sub_string = re.sub('[^A-Za-z]+', '', sub_string).lower()
    palindromes = set()
    for i in range(len(sub_string)):
        for j in range(i+6, min(i+9, len(sub_string)+1)):
            word = sub_string[i:j]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
