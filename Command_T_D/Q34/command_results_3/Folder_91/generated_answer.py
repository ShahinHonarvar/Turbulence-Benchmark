def find_original_set(S1, S2, S3, S4, S5):
    # Write your code here
    return {i for i in range(min(S1), max(S1) + 1)} | {j for j in range(min(S2), max(S2) + 1)} | {k for k in range(min(S3), max(S3) + 1)} | {l for l in range(min(S4), max(S4) + 1)} | {m for m in range(min(S5), max(S5) + 1)}
