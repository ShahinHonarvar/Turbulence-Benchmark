from typing import List


def return_vowels(s: str) -> List[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    sliced_s = s[170:645]
    if not sliced_s:
        return result
    for char in sliced_s:
        if char in vowels and 'E' < char <= '~':
            result.append(char)

    return result
