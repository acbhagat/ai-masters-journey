# Server_monitor.py
# This program monitors the CPU and Memory usage of a server and sends an alert if it exceeds a certain threshold.

def check_server(server, cpu, mem):
    """Checks the CPU and Memory usage of a server and returns a status message.

    """
    if cpu > 80 and mem > 85:
        return "HIGH", f"{server} CPU = {cpu}%  MEMORY = {mem}% - ALERT! System Failure Risk!"
    elif cpu > 80 or mem > 85:
        return "CRITICAL", f"{server} CPU = {cpu}%  MEMORY = {mem}% - ALERT! System has Critical Risk!"
    elif cpu > 50:
        return "WARNING", f"{server} CPU = {cpu}% MEMORY = {mem}% - CPU usage is high but Memory is Normal."
    else:
        return "OK", f"{server} CPU = {cpu}% MEMORY = {mem} - CPU amd Memory usage is normal."


servers = ["web-1", "db-1", "cache-1", "web-2"]  # List of servers being monitored
cpu_usage = [45, 85, 60, 40]  # Simulated CPU usage for each server
memory_usage = [90, 90, 40, 80]  # Simulated Memory usage for each server

# Initialize counters for different server statuses

counts = {
    "HIGH": 0,
    "CRITICAL": 0,
    "WARNING": 0,
    "OK": 0
}

print("=== Server Monitor ===")

# for i in range(len(servers)): # Loop through each server and check its CPU usage
for server, cpu, mem in zip(servers, cpu_usage, memory_usage):  # Loop through each server and check its CPU and Memory usage

    print(f"\nChecking {server}...")  # Print the server being checked
    status, message = check_server(server, cpu, mem)  # Call the check_server function to get the status and message for the server
    print(f"{status}: {message}")  # Print the status and message for the server
    counts[status] += 1  # Increment the counter for the corresponding status

print(f"\n=== Summary ===")  # Print the summary of server statuses
print(f"Total Servers: {len(servers)}")  # Print the total number of servers being monitored

for key, value in counts.items():  # Loop through the counts dictionary and print the count for each status
    print(f"{key}: {value}")
