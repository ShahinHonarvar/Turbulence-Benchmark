
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)):
        if string[i].isalpha():
            for j in range(i+1, len(string)):
                if (j-i) == 80:
                    substr = string[i:j]
                    if substr == substr[::-1]:
                        palindromes.add(substr)
    return palindromes
