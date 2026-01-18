def gap_check(N, nums):
    for k in range(1, 4):
        for i in range(len(nums) - k):
            if nums[i] == nums[i + k]:
                return nums[i]
                
    return -1

# --- Hard Coded Input ---
len_arr = 6
nums = [2, 1, 2, 5, 3, 2]

# --- Execution ---
print(gap_check(len_arr, nums))