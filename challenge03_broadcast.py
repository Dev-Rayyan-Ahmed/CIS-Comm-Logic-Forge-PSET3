import heapq

def solve_feed_optimized(N, Q, K, operations):
    #initializing data structures
    #unit_msgs: list of lists for each unit. 
    #Structure: (time, msg_id, value)
    unit_msgs = [[] for _ in range(N + 1)]
    
    #subs: tracking subscriptions {user: {sub_to: start_time}}
    subs = {}
    
    output = []
    
    current_time = 0
    msg_id_ctr = 1
    
    #processing all operations
    for op_str in operations:
        parts = op_str.split()
        op = parts[0]
        current_time += 1
        
        if op == 'B':
            u = int(parts[1])
            m = int(parts[2])
            
            #  storing message as tuple (time, id, val)
            unit_msgs[u].append((current_time, msg_id_ctr, m))
            msg_id_ctr += 1
            
            #keeping only K most recent messages
            if len(unit_msgs[u]) > K:
                unit_msgs[u].pop(0) 
                
        elif op == 'S':
            u = int(parts[1])
            v = int(parts[2])
            
            #initializing user dict if needed
            if u not in subs:
                subs[u] = {}
            
            #recording subscription time if new
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
            
            #using a max-heap to find top 10 newest
            #Python heap is min-heap, so we use negative time
            #Heap item: (-time, sender_id, index_in_sender_list)
            pq = []
            
            #helper to push newest valid message from a sender
            def push_sender_latest(sender_id, min_time_req):
                msgs = unit_msgs[sender_id]
                if msgs:
                    #checking the newest message first (end of list)
                    idx = len(msgs) - 1
                    msg_time = msgs[idx][0]
                    
                    #only adding if it meets visibility time requirement
                    if msg_time >= min_time_req:
                        heapq.heappush(pq, (-msg_time, sender_id, idx))

            #1. adding Self (always visible, min_time = 0)
            push_sender_latest(u, 0)
            
            #2. adding Subscriptions (visible if msg_time >= sub_start_time)
            if u in subs:
                for v, start_time in subs[u].items():
                    push_sender_latest(v, start_time)
            
            found_ids = []
            
            #extracting up to 10 newest messages
            while pq and len(found_ids) < 10:
                neg_time, sender, idx = heapq.heappop(pq)
                
                #getting the actual message ID
                #unit_msgs[sender][idx] is (time, id, val)
                msg_id = unit_msgs[sender][idx][1]
                found_ids.append(str(msg_id))
                
                #trying to push the NEXT older message from the same sender
                if idx > 0:
                    next_idx = idx - 1
                    next_msg = unit_msgs[sender][next_idx]
                    next_time = next_msg[0]
                    
                    #checking visibility constraint for this older message
                    #if sender is self, limit is 0. If sub, limit is start_time
                    limit_time = 0
                    if sender != u:
                         limit_time = subs[u][sender]
                    
                    if next_time >= limit_time:
                        heapq.heappush(pq, (-next_time, sender, next_idx))

            if not found_ids:
                output.append("EMPTY")
            else:
                output.append(" ".join(found_ids))
                
    return output

# --- Hard Coded Input ---
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
results = solve_feed_optimized(N, Q, K, operations)

#printing final answers
for line in results:
    print(line)