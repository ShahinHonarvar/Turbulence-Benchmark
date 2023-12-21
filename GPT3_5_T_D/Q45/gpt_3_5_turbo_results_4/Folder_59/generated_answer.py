
def palindromes_between_indices(string):
    words = set()
    letters = [char.lower() for char in string[8:10] if char.isalpha()]
    if len(letters) >= 2:
        for i in range(len(letters)):
            for j in range(i+1, len(letters)):
                palindrome = letters[i] + letters[j] + letters[j] + letters[i]
                words.add(palindrome)
    return words
