def compute_alerts(temp, K):
    n = len(temp)
    res = [0] * n
    
    # Keeping track of the nearest index for each temperature (0-100)
    # Initialize with infinity
    last_pos = [float('inf')] * 101 
    
    # iterating backwards from the last day
    for i in range(n - 1, -1, -1):
        curr = temp[i]
        nearest = float('inf')
        
        # Check for warmer days
        start_warm = curr + K
        if start_warm <= 100:
            for t in range(start_warm, 101):
                if last_pos[t] < nearest:
                    nearest = last_pos[t]
                    
        # Check for colder days
        end_cold = curr - K
        if end_cold >= 30:
            for t in range(30, end_cold + 1):
                if last_pos[t] < nearest:
                    nearest = last_pos[t]
        
        # store result
        if nearest != float('inf'):
            res[i] = nearest
        else:
            res[i] = 0
            
        # Update map
        last_pos[curr] = i
        
    return res


temp1 = [70, 75, 65, 80, 60]
K1 = 10
print(f"Test 1: {compute_alerts(temp1, K1)}")

temp2 = [30, 40, 50, 60]
K2 = 15
print(f"Test 2: {compute_alerts(temp2, K2)}")

temp3 = [50, 52, 54, 53]
K3 = 10
print(f"Test 3: {compute_alerts(temp3, K3)}")
