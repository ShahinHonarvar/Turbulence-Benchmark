
def palindromes_of_specific_lengths(string):
    string = string[:10].lower()
    palindromes = set()
    for length in range(3, 6):
        for start in range(10 - length):
            sub_string = string[start:start+length]
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                palindromes.add(sub_string)
    return palindromes
