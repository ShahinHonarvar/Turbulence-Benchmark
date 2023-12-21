from typing import List


def return_vowels(s: str) -> List[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    sliced_s = s[19:20]
    if not sliced_s:
        return result
    for char in sliced_s:
        if char in vowels and '<' < char <= 'p':
            result.append(char)

    return result
