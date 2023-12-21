def palindromes_between_indices(str):
    str = str[2:5]
    if not str:
        return set()
    if len(str) == 1:
        return {str}
    if len(str) == 2:
        return {str + str[::-1]}
    return {str + str[::-1], str[::-1] + str}
