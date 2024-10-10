def fcfs(tasks):
    tasks.sort(key=lambda x: x[1])  # Sort tasks by arrival time
    current_time = 0
    waiting_times = []
    schedule = []
    
    for task in tasks:
        name, arrival_time, burst_time, _, _ = task
        if current_time < arrival_time:
            current_time = arrival_time
        waiting_time = current_time - arrival_time
        waiting_times.append(waiting_time)
        schedule.append((name, current_time, burst_time))
        current_time += burst_time
    
    return {
        'schedule': schedule,
        'average_waiting_time': sum(waiting_times) / len(waiting_times)
    }

def sjf(tasks):
    tasks.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival time, then burst time
    current_time = 0
    waiting_times = []
    schedule = []
    remaining_tasks = tasks.copy()
    
    while remaining_tasks:
        available_tasks = [t for t in remaining_tasks if t[1] <= current_time]
        if not available_tasks:
            current_time = min(t[1] for t in remaining_tasks)
            continue
        
        task = min(available_tasks, key=lambda x: x[2])
        name, arrival_time, burst_time, _, _ = task
        waiting_time = current_time - arrival_time
        waiting_times.append(waiting_time)
        schedule.append((name, current_time, burst_time))
        current_time += burst_time
        remaining_tasks.remove(task)
    
    return {
        'schedule': schedule,
        'average_waiting_time': sum(waiting_times) / len(waiting_times)
    }

def srtf(tasks):
    current_time = 0
    remaining_tasks = [(name, arrival_time, burst_time, burst_time, priority, portfolio_impact) 
                       for name, arrival_time, burst_time, priority, portfolio_impact in tasks]
    completed_tasks = []
    schedule = []
    
    while remaining_tasks:
        available_tasks = [t for t in remaining_tasks if t[1] <= current_time]
        if not available_tasks:
            current_time = min(t[1] for t in remaining_tasks)
            continue
        
        task = min(available_tasks, key=lambda x: x[3])  # Sort by remaining time
        name, arrival_time, burst_time, remaining_time, priority, portfolio_impact = task
        
        next_arrival = min((t[1] for t in remaining_tasks if t[1] > current_time), default=float('inf'))
        run_time = min(remaining_time, next_arrival - current_time)
        
        schedule.append((name, current_time, run_time))
        current_time += run_time
        remaining_time -= run_time
        
        if remaining_time == 0:
            completed_tasks.append((name, arrival_time, burst_time, current_time - arrival_time - burst_time))
            remaining_tasks.remove(task)
        else:
            index = remaining_tasks.index(task)
            remaining_tasks[index] = (name, arrival_time, burst_time, remaining_time, priority, portfolio_impact)
    
    return {
        'schedule': schedule,
        'average_waiting_time': sum(t[3] for t in completed_tasks) / len(completed_tasks)
    }

def round_robin(tasks, time_quantum):
    current_time = 0
    remaining_tasks = [(name, arrival_time, burst_time, burst_time, priority, portfolio_impact) 
                       for name, arrival_time, burst_time, priority, portfolio_impact in tasks]
    completed_tasks = []
    schedule = []
    
    while remaining_tasks:
        task = remaining_tasks.pop(0)
        name, arrival_time, burst_time, remaining_time, priority, portfolio_impact = task
        
        if current_time < arrival_time:
            current_time = arrival_time
        
        run_time = min(remaining_time, time_quantum)
        schedule.append((name, current_time, run_time))
        current_time += run_time
        remaining_time -= run_time
        
        if remaining_time == 0:
            completed_tasks.append((name, arrival_time, burst_time, current_time - arrival_time - burst_time))
        else:
            remaining_tasks.append((name, arrival_time, burst_time, remaining_time, priority, portfolio_impact))
    
    return {
        'schedule': schedule,
        'average_waiting_time': sum(t[3] for t in completed_tasks) / len(completed_tasks)
    }

def priority_scheduling(tasks):
    current_time = 0
    remaining_tasks = [(name, arrival_time, burst_time, burst_time, priority, portfolio_impact) 
                       for name, arrival_time, burst_time, priority, portfolio_impact in tasks]
    completed_tasks = []
    schedule = []
    
    while remaining_tasks:
        available_tasks = [t for t in remaining_tasks if t[1] <= current_time]
        if not available_tasks:
            current_time = min(t[1] for t in remaining_tasks)
            continue
        
        task = max(available_tasks, key=lambda x: x[4])  # Sort by priority (higher number = higher priority)
        name, arrival_time, burst_time, remaining_time, priority, portfolio_impact = task
        
        schedule.append((name, current_time, remaining_time))
        current_time += remaining_time
        completed_tasks.append((name, arrival_time, burst_time, current_time - arrival_time - burst_time))
        remaining_tasks.remove(task)
    
    return {
        'schedule': schedule,
        'average_waiting_time': sum(t[3] for t in completed_tasks) / len(completed_tasks)
    }

def pbpm(tasks, market_volatility):
    current_time = 0
    remaining_tasks = [(name, arrival_time, burst_time, burst_time, priority, portfolio_impact) 
                       for name, arrival_time, burst_time, priority, portfolio_impact in tasks]
    completed_tasks = []
    schedule = []
    
    while remaining_tasks:
        available_tasks = [t for t in remaining_tasks if t[1] <= current_time]
        if not available_tasks:
            current_time = min(t[1] for t in remaining_tasks)
            continue
        
        task = max(available_tasks, key=lambda x: x[4] * (1 + x[5]) * (1 + market_volatility))
        name, arrival_time, burst_time, remaining_time, priority, portfolio_impact = task
        
        run_time = min(remaining_time, 2)  # Time slice of 2 units
        schedule.append((name, current_time, run_time))
        current_time += run_time
        remaining_time -= run_time
        
        if remaining_time == 0:
            completed_tasks.append((name, arrival_time, burst_time, current_time - arrival_time - burst_time))
            remaining_tasks.remove(task)
        else:
            index = remaining_tasks.index(task)
            remaining_tasks[index] = (name, arrival_time, burst_time, remaining_time, priority, portfolio_impact)
    
    return {
        'schedule': schedule,
        'average_waiting_time': sum(t[3] for t in completed_tasks) / len(completed_tasks)
    }

# Remove or comment out the main function and any print statements
# def main():
#     ...

# if __name__ == "__main__":
#     main()