
def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 7, len(string) + 1):
            if string[i:j] == string[i:j][::-1] and string[i:j].isalpha():
                palindromes.add(string[i:j])
    return palindromes
