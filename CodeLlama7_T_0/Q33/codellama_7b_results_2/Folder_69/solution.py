from typing import List


def return_vowels(s: str) -> List[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    sliced_s = s[641:872]
    if not sliced_s:
        return result
    for char in sliced_s:
        if char in vowels and '>' < char <= 'q':
            result.append(char)

    return result
