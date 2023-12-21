def find_original_set(x, y, z, a, b, c, d, e, f, g, h):
    return set(range(x, y)) | set(range(z, a)) | set(range(b, c)) | set(range(d, e)) | set(range(f, g)) | set(range(h, max(x, y, z, a, b, c, d, e, f, g, h) + 1))
