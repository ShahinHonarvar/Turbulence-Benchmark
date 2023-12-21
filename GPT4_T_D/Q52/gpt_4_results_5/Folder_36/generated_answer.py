
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    length = len(string)
    for i in range(length):
        for j in range(i+338, min(i + 677, length+1)):
            sub = string[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes
