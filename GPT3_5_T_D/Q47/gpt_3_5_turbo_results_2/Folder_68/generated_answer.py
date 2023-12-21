
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(min(51, len(string))):
        for j in range(i+50, min(i+101, len(string))):
            sub_string = string[i:j+1]
            if sub_string.lower() == sub_string.lower()[::-1] and sub_string.isalpha():
                palindromes.add(sub_string)
    return palindromes
