def detect_anagrams_naive(s, p):
    n = len(s)
    k = len(p)
    indices = []
    
    if k > n:
        return indices

    #sorting p for comparison
    target = sorted(p)

    #iterating through every possible window
    for i in range(n - k + 1):
       
        substring = s[i : i + k]
        if sorted(substring) == target:
            indices.append(i)
            
    return indices

# --- Hard Coded Input ---
s_input = "cbaebabacd"
p_input = "abc"

# --- Execution ---
result = detect_anagrams_naive(s_input, p_input)
print(result)