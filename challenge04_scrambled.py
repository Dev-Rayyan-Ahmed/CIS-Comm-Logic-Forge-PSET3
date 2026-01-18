def detect_anagrams(s, p):
    n = len(s)
    k = len(p)
    indices = []
    
    if k > n:
        return indices
        
    p_count = [0] * 26
    window_count = [0] * 26
    
    base = ord('a')
    
    #populating counts for p and the first window of s
    for i in range(k):
        p_count[ord(p[i]) - base] += 1
        window_count[ord(s[i]) - base] += 1
        
    #checking the very first window
    if p_count == window_count:
        indices.append(0)
        
    #sliding window across the rest of s
    #i represents the index of the character being removed
    for i in range(n - k):
        #removing the character that is sliding out (left)
        left_char = s[i]
        window_count[ord(left_char) - base] -= 1
        
        #adding the character that is sliding in (right)
        right_char = s[i + k]
        window_count[ord(right_char) - base] += 1
        
        #comparing the frequency arrays
        if p_count == window_count:
            indices.append(i + 1)
            
    return indices

# --- Hard Coded Input ---
s_input = "cbaebabacd"
p_input = "abc"

# --- Execution ---
result = detect_anagrams(s_input, p_input)
print(result)