def maxFreq(s, maxLetters, minSize, maxSize):
    """
    :type s: str
    :type maxLetters: int
    :type minSize: int
    :type maxSize: int
    :rtype: int
    """
    freq = defaultdict(int)
    max_occurrence = 0
    
    for i in range(len(s) - minSize + 1):
        sub = s[i:i+minSize]
        if len(set(sub)) <= maxLetters:
            freq[sub] += 1
            max_occurrence = max(max_occurrence, freq[sub])
    
    return max_occurrence