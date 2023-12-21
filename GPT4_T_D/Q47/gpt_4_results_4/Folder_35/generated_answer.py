
def palindromes_of_specific_lengths(s):
    substr = s[34:91]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i+14, min(i+40, len(substr)+1)):
            test_string = substr[i:j]
            if test_string.lower() == test_string[::-1].lower() and test_string.isalpha():
                palindromes.add(test_string)
    return palindromes
