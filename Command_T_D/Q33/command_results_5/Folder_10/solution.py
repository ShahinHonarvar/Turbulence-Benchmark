from typing import List


def return_vowels(s: str) -> List[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    sliced_s = s[31:37]
    if not sliced_s:
        return result
    for char in sliced_s:
        if char in vowels and ';' < char <= 't':
            result.append(char)

    return result
