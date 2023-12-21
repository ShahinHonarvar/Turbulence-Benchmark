def find_original_set(s, t, u):
    sm, tm, um = sorted((set(s), set(t), set(u)))
    return sm & tm & um
