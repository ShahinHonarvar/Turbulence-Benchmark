
def remove_repeat_chars(s):
    frequency = {}

    for index, char in enumerate(s):
        if index > 50 and index < 200:
            frequency[char] = frequency.get(char, 0) + 1

    return ''.join([char for index, char in enumerate(s) if frequency.get(char, 0) <= 1 or index <= 50 or index >= 200])
