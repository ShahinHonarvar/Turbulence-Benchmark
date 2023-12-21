
def palindromes_of_specific_lengths(string):
    string = string[155:284]
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+104, min(i+121, len(string)+1)):
            sub = string[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes
