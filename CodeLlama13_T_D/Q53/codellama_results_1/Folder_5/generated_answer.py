
def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j+1] == string[i:j+1][::-1]:
                palindromes.add(string[i:j+1])
    return palindromes
