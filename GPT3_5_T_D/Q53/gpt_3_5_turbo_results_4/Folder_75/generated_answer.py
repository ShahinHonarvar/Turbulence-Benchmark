
def palindrome_of_length_at_least_n(string):
    import re
    string = re.sub('[^a-zA-Z]', '', string)
    string = string.lower()
    palindromes = set()
    for i in range(len(string)-39):
        sub_string = string[i:i+40]
        if sub_string == sub_string[::-1]:
            palindromes.add(sub_string)
    return palindromes
