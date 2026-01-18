def mirrored(s):
    if not s:
        return ""
        
    start = 0
    end = 0

    def expand(left, right):
        # expanding outwards while characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # return length of the valid palindrome
        return right - left - 1
    
    for i in range(len(s)):
        # check odd length (center is i)
        len1 = expand(i, i)
        # check even length (center is between i and i+1)
        len2 = expand(i, i + 1)
        
        max_len = max(len1, len2)
        
        # update result if we found a longer one
        if max_len > (end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
            
    return s[start : end + 1]

# --- Hard Coded Input --
s_input = "babad"

# --- Execution ---
print("Mirrored Phrase: ",mirrored(s_input))