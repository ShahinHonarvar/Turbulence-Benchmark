
def palindromes_of_specific_lengths(string):
    string = string[:51].lower()  # Consider only the substring up to index 50 and convert to lowercase
    palindromes = set()
    for length in range(50, 101):
        for i in range(len(string) - length + 1):
            substring = string[i:i+length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
