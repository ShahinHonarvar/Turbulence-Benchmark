
def palindromes_of_specific_lengths(s):
    import re
    sub_string = s[18:88]
    sub_string = re.sub("[^a-zA-Z]+", "", sub_string)
    palindromes = set()
    for i in range(len(sub_string)):
        for j in range(i+38, i+61):
            if j > len(sub_string):
                break
            if sub_string[i:j].lower() == sub_string[i:j][::-1].lower():
                palindromes.add(sub_string[i:j])
    return palindromes
