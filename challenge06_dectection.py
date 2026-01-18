def solve_frequency(N, nums):
    
    target_count = N // 2

    counts = {}
    
    for x in nums:
        # incrementing  count 
        counts[x] = counts.get(x, 0) + 1
        
        if counts[x] == 2:
            return x
            
    return -1

# --- Hard Coded Input ---
len_arr = 6
nums = [2, 1, 2, 5, 3, 2]

# --- Execution ---
print(solve_frequency(len_arr, nums))