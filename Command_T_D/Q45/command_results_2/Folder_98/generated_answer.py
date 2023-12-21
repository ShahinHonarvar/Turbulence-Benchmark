def palindromes_between_indices(str1):
    result = set()
    for i in range(3, 5):
        for j in range(3, 5):
            for c in str1[i:j]:
                result.add(c.lower() + str1[i:j][::-1])
    return result
