
def palindromes_between_indices(string):
    result = set()
    letters = [char.lower() for char in string[2:4] if char.isalpha()]
    if len(letters) >= 3:
        for i in range(len(letters)-2):
            for j in range(i+2, len(letters)):
                palindrome = ''.join(letters[i:j+1] + letters[i:j+1][::-1])
                result.add(palindrome)
    return result
