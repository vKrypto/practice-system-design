from collections import deque


    
def getTimes(entry_times, directions):
    result_times = [0] * len(entry_times)

    end_time = max(entry_times, default=0)
    if end_time == 0:
        return result_times

    entrance_queue = deque()
    exit_queue = deque()

    current_index = 0
    turnstile_state = 0

    for current_time in range(end_time + 1):
        while current_index < len(entry_times) and entry_times[current_index] == current_time:
            if directions[current_index] == 0:
                entrance_queue.append(current_index)
            if directions[current_index] == 1:
                exit_queue.append(current_index)
            current_index += 1
            if current_index == len(entry_times):
                break

        no_person_on_turnstile = len(entrance_queue) + len(exit_queue) == 0
        if no_person_on_turnstile:
            turnstile_state = 0

        if turnstile_state == 1 or len(exit_queue) == 0:
            if len(entrance_queue) > 0:
                next_person_index = entrance_queue.popleft()
                result_times[next_person_index] = current_time
                turnstile_state = 1
            else:
                if len(exit_queue) > 0:
                    next_person_index = exit_queue.popleft()
                    result_times[next_person_index] = current_time
                    turnstile_state = 2
        else:
            if len(exit_queue) > 0:
                next_person_index = exit_queue.popleft()
                result_times[next_person_index] = current_time
                turnstile_state = 2

    if len(entrance_queue) > 0:
        new_end_time = end_time
        while len(entrance_queue) > 0:
            next_person_index = entrance_queue.popleft()
            result_times[next_person_index] = new_end_time + 1
            new_end_time += 1

    return result_times


def calculate_turnstile_times(entry_times, directions):
    entry_queue, exit_queue = [], []
    result_times = [0] * len(entry_times)

    for i, t in enumerate(entry_times):
        if directions[i] == 1:
            exit_queue.append([entry_times[i], i])
        else:
            entry_queue.append([entry_times[i], i])
    
    time_counter, last_turn = 0, -1
    while exit_queue or entry_queue:
        if exit_queue and exit_queue[0][0] <= time_counter and \
           (last_turn == -1 or last_turn == 1 or not entry_queue or 
           (last_turn == 0 and entry_queue[0][0] > time_counter)):
            result_times[exit_queue[0][1]] = time_counter
            last_turn = 1
            exit_queue.pop(0)
        elif entry_queue and entry_queue[0][0] <= time_counter:
            result_times[entry_queue[0][1]] = time_counter
            last_turn = 0
            entry_queue.pop(0)
        else:
            last_turn = -1

        time_counter += 1
    
    return result_times



def getTimes(arr_times, directions):
    n = len(arr_times)
    q_enter, q_exit = deque(), deque()
    
    for i, d in enumerate(directions):
        if d == 0:
            q_enter.appendleft(i)
        else:
            q_exit.appendleft(i)
    
    t = 0
    prev_dir = -1
    ans = [-1] * n
    
    while q_enter and q_exit:
        enter_time, exit_time = arr_times[q_enter[-1]], arr_times[q_exit[-1]]
        
        if enter_time > t and exit_time > t:
            if exit_time <= enter_time:
                t = exit_time
                ans[q_exit.pop()] = t
                prev_dir = 1
            else:
                t = enter_time
                ans[q_enter.pop()] = t
                prev_dir = 0
        elif enter_time > t:
            ans[q_exit.pop()] = t
            prev_dir = 1
        elif exit_time > t:
            ans[q_enter.pop()] = t
            prev_dir = 0
        else:
            if prev_dir == -1 or prev_dir == 1:
                ans[q_exit.pop()] = t
            else:
                ans[q_enter.pop()] = t
        t += 1

    remaining_queue = q_enter if q_enter else q_exit
    while remaining_queue:
        qt = arr_times[remaining_queue[-1]]
        if qt > t:
            t = qt
        ans[remaining_queue.pop()] = t
        t += 1
    
    return ans

# Example usage
time = [1, 2, 3]
directions = [0, 1, 1]
result = getTimes([0, 0, 1, 5], [0, 1, 1, 0])
print(result)
