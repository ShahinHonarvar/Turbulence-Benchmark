def palindromes_of_specific_lengths(text):
    letters = "abcdefghijklmnopqrstuvwxyz"
    start, end = 26, 90
    length = 27
    result = set()
    while length <= 58:
        for i in range(start, end + 1):
            temp = text[i:i + length].lower()
            if temp[::-1] == temp:
                result.add(temp)
        length += 1
    return result
