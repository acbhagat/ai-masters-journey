"""
If-else are the control structures that allow us to execute different code based on certain conditions.
The basic syntax of an if-else statement is as follows:
if it rains:
    take an umbrella
else:
    enjoy the sunshine

In this example, if the condition "it rains" is true, the code block under the if statement will be executed, and you will take an umbrella. If the condition is false (i.e., it does not rain), the code block under the else statement will be executed, and you will enjoy the sunshine.

Cpu_usage = 85

If cpu_usage > 80:
    print("Warning: CPU usage is high!")
else:
    print("CPU usage is normal.")

In this example, we check if the CPU usage is greater than 80. If it is, we print a warning message.
Otherwise, we print that the CPU usage is normal.

Used everywhere:
alert systems, decision-making, user input validation, and more.
They are fundamental for controlling the flow of a program based on conditions.
"""

cpu_usage = 75

if cpu_usage > 80:
    print("Warning: CPU usage is high!")
elif cpu_usage > 50:
    print("CPU usage is moderate.")
else:
    print("CPU usage is normal.")


