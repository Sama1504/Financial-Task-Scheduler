import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scheduling_algorithms import (
    fcfs, sjf, srtf, round_robin, priority_scheduling, pbpm
)

st.set_page_config(page_title="Financial Task Scheduler", layout="wide")

# Custom CSS for financial theme
st.markdown("""
<style>
    .stApp {
        background-color: #18191AFF;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
    }
    .stSelectbox {
        background-color: #18191AFF;
    }
</style>
""", unsafe_allow_html=True)

st.title("Financial Task Scheduler")

# Sidebar for algorithm selection and parameters
st.sidebar.header("Scheduling Options")
algorithm = st.sidebar.selectbox(
    "Select Scheduling Algorithm",
    ["FCFS", "SJF", "SRTF", "Round Robin", "Priority Scheduling", "PBPM"]
)

time_quantum = None
market_volatility = None

if algorithm == "Round Robin":
    time_quantum = st.sidebar.number_input("Time Quantum", min_value=1, value=2)
elif algorithm == "PBPM":
    market_volatility = st.sidebar.slider("Market Volatility", 0.0, 1.0, 0.5, 0.01)

# Task input form
st.header("Add Financial Task")
with st.form("task_form"):
    col1, col2 = st.columns(2)
    with col1:
        task_name = st.text_input("Task Name")
        arrival_time = st.number_input("Arrival Time", min_value=0, value=0)
        burst_time = st.number_input("Burst Time", min_value=1, value=1)
    with col2:
        priority = st.number_input("Priority", min_value=1, value=1)
        task_type = st.selectbox("Task Type", ["Trade Execution", "Risk Assessment", "Portfolio Rebalancing", "Market Analysis"])
        portfolio_impact = st.number_input("Portfolio Impact", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    
    submitted = st.form_submit_button("Add Task")

# Initialize session state for tasks if not exists
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Add task to the list when form is submitted
if submitted:
    st.session_state.tasks.append({
        "name": task_name,
        "arrival_time": arrival_time,
        "burst_time": burst_time,
        "priority": priority,
        "task_type": task_type,
        "portfolio_impact": portfolio_impact
    })

# Display task list
st.header("Task List")
if st.session_state.tasks:
    df = pd.DataFrame(st.session_state.tasks)
    st.dataframe(df)
    
    if st.button("Clear All Tasks"):
        st.session_state.tasks = []
        st.experimental_rerun()
else:
    st.info("No tasks added yet. Use the form above to add tasks.")

# Run scheduling algorithm
if st.button("Run Scheduling Algorithm"):
    if not st.session_state.tasks:
        st.warning("Please add tasks before running the algorithm.")
    else:
        # Convert tasks to the format expected by scheduling algorithms
        tasks = [
            (task["name"], task["arrival_time"], task["burst_time"], task["priority"], task["portfolio_impact"])
            for task in st.session_state.tasks
        ]
        
        # Run the selected algorithm
        if algorithm == "FCFS":
            result = fcfs(tasks)
        elif algorithm == "SJF":
            result = sjf(tasks)
        elif algorithm == "SRTF":
            result = srtf(tasks)
        elif algorithm == "Round Robin":
            result = round_robin(tasks, time_quantum)
        elif algorithm == "Priority Scheduling":
            result = priority_scheduling(tasks)
        elif algorithm == "PBPM":
            result = pbpm(tasks, market_volatility)
        
        # Display results
        st.subheader("Scheduling Results")
        st.write(f"Average Waiting Time: {result['average_waiting_time']:.2f}")
        
        # Visualize task execution
        fig, ax = plt.subplots(figsize=(12, 6))
        for task in result['schedule']:
            ax.barh(task[0], task[2], left=task[1], height=0.5)
        ax.set_xlabel("Time")
        ax.set_ylabel("Tasks")
        ax.set_title("Task Execution Timeline")
        st.pyplot(fig)

# Help section
with st.expander("Help & Documentation"):
    st.markdown("""
    ## Scheduling Algorithms
    
    - **FCFS (First-Come, First-Served)**: Tasks are executed in the order they arrive.
    - **SJF (Shortest Job First)**: Tasks with the shortest burst time are executed first.
    - **SRTF (Shortest Remaining Time First)**: Preemptive version of SJF.
    - **Round Robin**: Tasks are executed in a circular order for a fixed time quantum.
    - **Priority Scheduling**: Tasks with higher priority are executed first.
    - **PBPM (Portfolio-Based Priority Management)**: Tasks are scheduled based on their portfolio impact and market volatility.
    
    ## Parameters
    
    - **Time Quantum**: Used in Round Robin scheduling to determine how long each task runs before being preempted.
    - **Market Volatility**: Used in PBPM to adjust the importance of portfolio impact in scheduling decisions.
    
    ## Task Properties
    
    - **Arrival Time**: When the task becomes available for execution.
    - **Burst Time**: The time required to complete the task.
    - **Priority**: The importance of the task (higher number means higher priority).
    - **Portfolio Impact**: The potential effect of the task on the portfolio (0.0 to 1.0).
    """)

# Error handling and validation are implemented within the Streamlit widgets