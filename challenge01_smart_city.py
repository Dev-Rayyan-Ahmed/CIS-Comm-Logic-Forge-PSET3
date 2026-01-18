def compute_alerts(temp, K):
    n = len(temp)
    res = [0] * n
    
    # mapping each temperaturee (0-100) to its most recently seen index
    last_pos = [float('inf')] * 101 
    
    # iterating backwards to find nearest future day
    for i in range(n - 1, -1, -1):
        curr = temp[i]
        nearest = float('inf')
        
        # Check warmer range
        start_warm = curr + K
        if start_warm <= 100:
            for t in range(start_warm, 101):
                if last_pos[t] < nearest:
                    nearest = last_pos[t]
                    
        # Check colder range
        end_cold = curr - K
        if end_cold >= 30:
            for t in range(30, end_cold + 1):
                if last_pos[t] < nearest:
                    nearest = last_pos[t]
        
        # Store result
        if nearest != float('inf'):
            res[i] = nearest
        else:
            res[i] = 0
            
        #updateing map 
        last_pos[curr] = i
        
    return res

def solve():
    #Read N, K, Q
    line1 = input().split()
    if not line1: return
    N = int(line1[0])
    K = int(line1[1])
    Q = int(line1[2])

    #Read Temperature Array
    temp = list(map(int, input().split()))

    alerts = compute_alerts(temp, K)

    pref = [0] * N
    running_total = 0
    for i in range(N):
        if alerts[i] != 0:
            running_total += 1
        pref[i] = running_total

    results = [] # to store answers
    
    for _ in range(Q):
        query = input().split()
        type_query = query[0]

        if type_query == "NEXT":
            X = int(query[1])
            ans = alerts[X]
            if ans == 0:
                results.append("No Alert")
            else:
                results.append(str(ans))

        elif type_query == "COUNT":
            L = int(query[1])
            R = int(query[2])
            
            val_R = pref[R]
            val_L = pref[L - 1] if L > 0 else 0
            results.append(str(val_R - val_L))

    #printing all results..
    print("\n".join(results))

if __name__ == "__main__":
    solve()