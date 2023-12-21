def find_original_set(s1, s2, s3, s4, s5, s6, s7, s8):
    return min(s1 | s2 | s3 | s4 | s5 | s6 | s7 | s8,
                s1 | s2 | s3 | s4 | s5 | s6 | s7 | s8 | {i for i in range(1, 10 ** 5 + 1) if all(j in s for j in range(i))})
