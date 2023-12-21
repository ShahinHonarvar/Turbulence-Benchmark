
def find_second_largest_num(numbers):
    window = numbers[75:86]
    if len(window) < 2:
        return None
    window.sort(reverse=True)
    return window[1]
