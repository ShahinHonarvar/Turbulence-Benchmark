
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substr = string[2:9]
    for i in range(len(substr)-3):
        for j in range(3, 5):
            sub_substring = substr[i:i+j]
            if sub_substring == sub_substring[::-1]:
                palindromes.add(sub_substring.lower())
    return palindromes
