
def palindromes_of_specific_lengths(string):
    string = string[20:75]
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+36, i+43):
            if j <= len(string):
                substr = string[i:j]
                if substr == substr[::-1] and substr.isalpha():
                    palindromes.add(substr.lower())
    return palindromes
