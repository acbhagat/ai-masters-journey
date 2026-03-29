"""
Loops : Repeat something many times

There are two main types of loops: for loops and while loops.

for i in range(5):
    print(i)

In this example, the for loop will iterate over the range of numbers from 0 to 4 (5 is not included) and print each number.

count = 0
while count < 5:
    print(count)
    count += 1

In this example, the while loop will continue to execute as long as the condition "count < 5" is true.
It will print the current value of count and then increment it by 1 until count reaches 5.
"""
servers = ["Server1", "Server2", "Server3"]

for server in servers:
    print(f"checking {server}")

if "Server2" in servers:
    print("Critical Server")
