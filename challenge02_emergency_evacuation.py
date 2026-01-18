def solve_greedy(N, Q, limit, weights, priority, queries):
    #combining weights and priorities
    people = []
    for i in range(N):
        people.append({'w': weights[i], 'p': priority[i]})
        
    #sorting people list
    people.sort(key=lambda x: x['w'])
    
    left = 0
    right = N - 1
    max_pairs = 0
    
    #counting max possible pairs
    while left < right:
        w_sum = people[left]['w'] + people[right]['w']
        #checking for priority clash
        conflict = (people[left]['p'] == 1 and people[right]['p'] == 1)
        
        if w_sum <= limit and not conflict:
            #incrementing pair count
            max_pairs += 1
            left += 1
            right -= 1
        else:
            #skipping heavy person
            right -= 1
            
    #calculating boats needed
    min_boats = N - max_pairs
    
    results = []
    #processing query list
    for q in queries:
        parts = q.split()
        
        if parts[0] == "CANPAIR":
            x, y = int(parts[1]), int(parts[2])
            w_check = weights[x] + weights[y] <= limit
            #validating priorities
            p_check = not (priority[x] == 1 and priority[y] == 1)
            
            if w_check and p_check:
                results.append("Yes")
            else:
                results.append("No")
                
        elif parts[0] == "REMAINING":
            B = int(parts[1])
            
            if B <= max_pairs:
                #filling boats with pairs
                evacuated = B * 2
            else:
                #taking pairs and singles
                evacuated = max_pairs * 2
                singles = min(B - max_pairs, N - evacuated)
                evacuated += singles
                
            results.append(str(N - evacuated))

    return min_boats, results

# --- Input Data ---
weights = [30, 50, 60, 40, 70, 80]
priority = [1, 0, 1, 0, 0, 1]
limit = 100
queries = ["CANPAIR 0 1", "CANPAIR 0 2", "REMAINING 2"]

# --- Execution ---
min_boats, answers = solve_greedy(6, 3, limit, weights, priority, queries)

print("Minimum boats =", min_boats)
print('\n'.join(answers))