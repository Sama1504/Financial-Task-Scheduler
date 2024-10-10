## Project Overview

This project implements a Financial Task Scheduler that applies various Operating System scheduling algorithms to manage and prioritize financial tasks. It serves as a prototype to demonstrate how OS concepts can be used in Finance and Investment.

## Operating System Concepts Applied

The scheduler implements the following OS scheduling algorithms:

1. First-Come, First-Served (FCFS)
2. Shortest Job First (SJF)
3. Shortest Remaining Time First (SRTF)
4. Round Robin
5. Priority Scheduling (Preemptive)
6. Portfolio-Based Priority Management (PBPM) - A custom algorithm

## Domain: Finance and Investment

In the context of finance and investment, task scheduling is crucial for managing various operations such as:

- Trade Execution
- Risk Assessment
- Portfolio Rebalancing
- Market Analysis

The scheduler allows prioritization based on task urgency, potential portfolio impact, and market volatility.

## Implementation

The project is implemented in Python, utilizing the following libraries:

- Streamlit: For creating the interactive web application
- Pandas: For data manipulation and display
- Matplotlib: For visualizing the task execution timeline

## Key Files

1. `app.py`: The main Streamlit application that provides the user interface.
2. `scheduling_algorithms.py`: Contains the implementation of all scheduling algorithms.
3. `requirements.txt`: Lists all the Python dependencies required to run the project.

## Features

- Add financial tasks with properties such as name, arrival time, burst time, priority, task type, and portfolio impact.
- Choose from multiple scheduling algorithms to organize tasks.
- Visualize the task execution timeline.
- Calculate and display average waiting time for tasks.
- Adjust parameters like time quantum (for Round Robin) and market volatility (for PBPM).

 ## How to Run

1. Clone the repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Usage

1. Add tasks using the input form.
2. Select a scheduling algorithm from the sidebar.
3. Adjust any necessary parameters (e.g., time quantum for Round Robin).
4. Click "Run Scheduling Algorithm" to see the results.
5. View the task execution timeline and average waiting time.
   
## Future Enhancements

- Implement more domain-specific scheduling algorithms.
- Add real-time data integration for market conditions.
- Enhance visualization with more detailed performance metrics.
- Implement task dependencies and resource allocation.

