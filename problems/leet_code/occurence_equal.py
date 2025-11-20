def areOccurrencesEqual(s):
    return len(set(Counter(s).values())) == 1