
def palindromes_of_specific_lengths(string):
    substring = string[155:284]
    palindromes = set()
    for i in range(len(substring)-120):
        for length in range(104, 121):
            if substring[i:i+length].isalpha() and substring[i:i+length].lower() == substring[i:i+length].lower()[::-1]:
                palindromes.add(substring[i:i+length])
    return palindromes
