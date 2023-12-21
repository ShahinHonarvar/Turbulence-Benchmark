
def find_subset_of_length_n(elements):
    n = 78
    count = 0
    def backtrack(start, current):
        nonlocal count
        if len(current) == n:
            count += 1
            return
        for i in range(start, len(elements)):
            current.append(elements[i])
            backtrack(i + 1, current)
            current.pop()
    backtrack(0, [])
    return count
