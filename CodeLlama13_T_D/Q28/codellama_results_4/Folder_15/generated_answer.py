
def return_nth_smallest_ascii(string):
    count = {}
    for i in range(0, 6):
        for char in string[i]:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
    nth_smallest = sorted(count.items(), key=lambda x: x[1])[5][0]
    return nth_smallest
