def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    counts = [0] * 26
    for ch in s1:
        counts[ord(ch) - ord('a')] += 1
    for ch in s2:
        counts[ord(ch) - ord('a')] -= 1

    for c in counts:
        if c != 0:
            return False
    return True