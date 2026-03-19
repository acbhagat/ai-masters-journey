# Server_monitor.py
# This program monitors the CPU and Memory usage of a server and sends an alert if it exceeds a certain threshold.

servers = ["web-1", "db-1", "cache-1"] # List of servers being monitored
cpu_usage = [45, 85, 60] # Simulated CPU usage for each server
memory_usage = [90, 90, 40] # Simulated Memory usage for each server

print("=== Server Monitor ===")

for i in range(len(servers)): # Loop through each server and check its CPU usage
    server = servers[i] # Get the server name
    cpu = cpu_usage[i] # Get the CPU usage for the server
    mem = memory_usage[i] # Get the Memory usage for the server

    print(f"\nChecking {server}...") # Print the server being checked

    if cpu > 80 and mem > 85: # If CPU usage exceeds 80%, and memory 85% then send an alert
        print(f"HIGH: {server} CPU = {cpu}%  MEMORY = {mem}% - ALERT! System Failure Risk!") # Print alert message
    elif cpu > 80 or mem > 85: # If CPU usage exceeds 80% or memory usage exceeds 85%, print a Critical warning
        print(f"CRITICAL: {server} CPU = {cpu}%  MEMORY = {mem}% - ALERT! System has Critical Risk!") # Print warning message
    elif cpu > 50: # If CPU usage is between 50% and 80%, print a warning
        print(f"WARNING: {server} CPU = {cpu}% - CPU usage is high.") # Print warning message
    else: # If CPU usage is 50% or below, print that everything is normal
        print(f"OK: {server} CPU = {cpu}% - CPU usage is normal.") # Print normal-message




