
def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 96, len(string)):
            if string[i:j+1] == string[i:j+1][::-1] and string[i:j+1].isalpha():
                palindromes.add(string[i:j+1])
    return palindromes
