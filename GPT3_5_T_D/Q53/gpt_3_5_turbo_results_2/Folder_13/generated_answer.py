

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()

    for i in range(len(string)-51):
        if string[i:i+52] == string[i:i+52][::-1]:
            palindromes.add(string[i:i+52])

    return palindromes
