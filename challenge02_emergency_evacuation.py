def solve_simulation(N, Q, limit, weights, priority, queries):
    #pairing data together
    people = []
    for i in range(N):
        people.append({'w': weights[i], 'p': priority[i]})
    
    #sorting by weight
    people.sort(key=lambda x: x['w'])

    boats = 0
    #copying list for simulation
    remaining = list(people)

    #  processing people until none left
    while remaining:
        boats += 1
        #taking the heaviest person
        heaviest = remaining.pop()
        
        if not remaining:
            break
            
        #finding the lightest person
        lightest = remaining[0]
        
        # checking constraints
        w_sum = heaviest['w'] + lightest['w']
        p_conflict = (heaviest['p'] == 1 and lightest['p'] == 1)
        
        if w_sum <= limit and not p_conflict:
            #removing the paired person
            remaining.pop(0)

    results = []
    # answering queries
    for q in queries:
        parts = q.split()
        
        if parts[0] == "CANPAIR":
            x, y = int(parts[1]), int(parts[2])
            val_w = weights[x] + weights[y]
            #checking priority conflict
            conflict = (priority[x] == 1 and priority[y] == 1)
            
            if val_w <= limit and not conflict:
                results.append("Yes")
            else:
                results.append("No")

        elif parts[0] == "REMAINING":
            B = int(parts[1])
            #calculating max pairs possible
            max_pairs = N - boats
            
            if B <= max_pairs:
                evacuated = B * 2
            else:
                #taking all pairs plus singles
                evacuated = max_pairs * 2
                leftover_boats = B - max_pairs
                leftover_people = N - evacuated
                evacuated += min(leftover_boats, leftover_people)
                
            results.append(str(N - evacuated))
            
    return boats, results

# --- Input Data ---
weights = [30, 50, 60, 40, 70, 80]
priority = [1, 0, 1, 0, 0, 1]
limit = 100
queries = ["CANPAIR 0 1", "CANPAIR 0 2", "REMAINING 2"]

# --- Execution ---
min_boats, answers = solve_simulation(6, 3, limit, weights, priority, queries)

print("Minimum boats =", min_boats)
print('\n'.join(answers))