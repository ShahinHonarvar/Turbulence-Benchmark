
def return_nth_smallest_ascii(s):
    count = {}
    for i in range(34, 82):
        if s[i-1] not in count:
            count[s[i-1]] = 0
        count[s[i-1]] += 1
    nth_smallest = sorted(count, key=lambda x: ord(x))[11]
    return nth_smallest
