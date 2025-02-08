# System Monitoring Tool
by Muhammad Shaaf Yousaf

This program is written in C language and it displays **UNIX** system information in real time using graphs.

With this program, you can view the following system information:
- Memory Usage (in GB)
- CPU Utilization (in %)
- Number of CPU cores and max CPU frequency (in GHz)

This program reads data from the following UNIX files:
- /proc/meminfo
- /proc/stat
- /proc/cpuinfo
- /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq

The graphs in the terminal are all updated using **ANSI** escape sequences.
You need to have a terminal that supports **ANSI** escape sequences, and access to a **UNIX** system, and **GCC** (or any alternative C compiler).

## Code Compilation
To compile the code you should use the following command in a UNIX terminal:
- "gcc main.c --std=c99"

## Code Usage
You have access to the following command line arguments (Flags) that the program accepts:
- "--cpu" (Displays CPU Utilization Graph in %)
- "--memory" (Displays Memory Usage Graph in GB)
- "--cores" (Returns Number of CPU Cores along with Max CPU Frequency)
- "--samples=N" (If used the value **N** will indicate how many statistics are collected)
- "--tdelay=T" (If used the value **T** will indicate how frequently to collect satatistics)

**It should be noted that the DEFAULT value of samples = 20 and tdelay = 500000 microseconds**

**It should also be noted that by DEFAULT all statistics are displayed (Memory, CPU, Cores). If a command line argument is passed to display a specific statistic, then the program defaults to only displaying that specific statistic**

**Number of samples and tdelay are also accepted in the format: "./myMonitoringTool [N [T]]"**

## Example Usage of Commands
Take as example:**./myMonitoringTool 50 600000 --cpu --tdelay=100**

Note that "50" is read as the number of samples, "600000" is read as tdelay in microseconds, and the extra "--tdelay=100" command is ignored.

We also observe the "--cpu" command, this indicates that the program will now only display the CPU graph.

## How it works
**Memory Usage Function works in the following way:**
- This Program gets its column values and stores its row values in the main function.
- The function reads "/proc/meminfo" and extracts MemTotal, MemFree, MemAvailable, Buffers, Cached.
- The function then calculates the Total Memory used using the formula "Used = Total - Available"
- The function then calculates a "NICE Value" with which it draws the Graph (with 10 rows) that can fit our Memroy usage.
- The function dividing "USED"/"NICE Value" and multiplying by 10 to get row number and it gets.
- Then the program decides where in the graph should "#" be printed based on the calculated row number and the column number that was passed from the Main function.

**CPU Utilization Function works in the following way:**
- This function gets its N-1 Total CPU Time, and idle_time query from the Main Fuction (where it stores the time back to for use in the next cycle).
- When the function runs, it reads "/proc/stat" and extracts the cpu times -> user, nice, sys, idle, iowait, irq, softirq.
- The function then calculates the Total CPU Time by adding all of the cpu times above.
- The function then calculates a Change in Total CPU Time by subtracting the value passed form main function and its own value.
- The function then calculated the Total CPU Utilization by dividing change_in_idle/change_in_total_time and some other numbers to make it nicer.
- The function calculates the row by dividing "Total CPU Utilization"/ 10.
- Then the program decides where in the graph should ":" be printed based on the calculated row number and the column number that was passed from the Main function.

**Cores Function works in the following way:**
- This function read the maximum cpu frequency from the file "/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq".
- It also calculates the number of CPU Cores from "/proc/cpuinfo". Due to the way my program reads the file, it will add 1 to the number of cores.
- The function now displays the Max CPU Frequency
- After which it now prints a number of boxes not more than the total number of cores we calculated.

**Role of the Main Function:**
The Main function acts as a helper function for all of these comands to work as intended.

The Main function calculates how much time is left and how many more samples need to be printed. This information is passed along to the functions along with the column number for "Memory" and "CPU" function.




This README file is intended to give a High-Level Overview of my system_monitory tool, how to compile it, and how its various options allows the user to monitor system statistics.
