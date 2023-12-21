from typing import List


def return_vowels(s: str) -> List[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    sliced_s = s[71:88]
    if not sliced_s:
        return result
    for char in sliced_s:
        if char in vowels and '9' < char <= 'P':
            result.append(char)

    return result
