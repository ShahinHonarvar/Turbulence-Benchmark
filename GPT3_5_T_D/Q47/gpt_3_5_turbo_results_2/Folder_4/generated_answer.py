
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(12, 93):
        substring = string[i:i+66]
        for length in range(17, 67):
            sub = substring[:length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes
