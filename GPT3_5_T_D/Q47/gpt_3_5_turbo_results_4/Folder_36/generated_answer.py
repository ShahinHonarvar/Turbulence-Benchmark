
def palindromes_of_specific_lengths(string):
    substring = string[124:284]
    palindromes = set()
    for length in range(115, 135):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes
