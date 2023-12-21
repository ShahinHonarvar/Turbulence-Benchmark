
def palindromes_between_indices(string):
    arr = []
    for char in string[6:10]:
        if char.isalpha():
            arr.append(char.lower())
    palindromes = set()
    for i in range(len(arr)):
        for j in range(len(arr)):
            word = arr[i] + arr[j]
            if word[::-1].lower() == word.lower() and len(word) >= 3:
                palindromes.add(word)
    return palindromes
