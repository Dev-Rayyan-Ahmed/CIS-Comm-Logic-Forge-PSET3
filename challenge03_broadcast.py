def solve_feed(N, Q, K, operations):
    #initializing data structures
    #unit_msgs: stores messages sent by each unit (msg_id, val, time)
    unit_msgs = [[] for _ in range(N + 1)]
    
    #subs: stores active subscriptions {user: {sub_to: start_time}}
    subs = {}
    
    output = []
    
    current_time = 0
    msg_id_ctr = 1
    
    #processing operations
    for op_str in operations:
        parts = op_str.split()
        op = parts[0]
        current_time += 1
        
        if op == 'B':
            u = int(parts[1])
            m = int(parts[2])
            
            #creating message tuple: (time, id, val)
            msg = {'time': current_time, 'id': msg_id_ctr, 'val': m}
            msg_id_ctr += 1
            
            #storing message with k limit check
            unit_msgs[u].append(msg)
            if len(unit_msgs[u]) > K:
                unit_msgs[u].pop(0) #removing oldest
                
        elif op == 'S':
            u = int(parts[1])
            v = int(parts[2])
            
            #setting subscription start time
            if u not in subs:
                subs[u] = {}
            #only update start time if not already subscribed
            if v not in subs[u]:
                subs[u][v] = current_time
                
        elif op == 'U':
            u = int(parts[1])
            v = int(parts[2])
            
            #removing subscription
            if u in subs and v in subs[u]:
                del subs[u][v]
                
        elif op == 'F':
            u = int(parts[1])
            visible = []
            
            #fetching own messages (always visible)
            visible.extend(unit_msgs[u])
            
            #fetching subscription messages
            if u in subs:
                for v, start_time in subs[u].items():
                    #checking only messages from v sent after subscription started
                    for msg in unit_msgs[v]:
                        if msg['time'] >= start_time:
                            visible.append(msg)
            
            visible.sort(key=lambda x: x['time'], reverse=True)
            
            #taking top 10
            top_10 = visible[:10]
            
            if not top_10:
                output.append("EMPTY")
            else:
                ids = [str(m['id']) for m in top_10]
                output.append(" ".join(ids))
                
    return output

# --- HardCoded Input ---
N = 3
Q = 9
K = 2
operations = [
    "S 1 2",
    "S 1 3",
    "B 2 5",
    "B 3 9",
    "F 1",
    "U 1 2",
    "B 3 6",
    "F 1",
    "F 2"
]

# --- Execution ---
results = solve_feed(N, Q, K, operations)

#printing results
for line in results:
    print(line)