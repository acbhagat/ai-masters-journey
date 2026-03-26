# This is a Revision Project for the Python Basics section of the Bootcamp Foundations course. It is designed to test your understanding of the concepts covered in the course.

servers = ["web-1", "db-1", "cache-1"]
cpu_usage = [80, 60, 90]
memory_usage = [85, 70, 95]

high = 0
working = 0
ok = 0
critical_system = 0

print("=== Revision Project: Server Health Check ===")

for i in range(len(servers)):

    server = servers[i]
    cpu = cpu_usage[i]
    memory = memory_usage[i]

    print(f"Checking {server}...")

    if server == "db-1":
        print("Critical System: Database Server")
        critical_system += 1
    else:
        print("Non-Critical System")

    # Operator + Conditional Statements
    if cpu > 80 and memory > 85:
        print("HIGH RISK: CPU and Memory usage are both high!")
        high += 1
    elif cpu > 50:
        print("WORKING: CPU usage is moderate.")
        working += 1
    else:
        print("OK: CPU usage is low.")
        ok += 1

    if ok > 0:
        continue
    else:
        print("No system in Ok state, Please Check Servers")

print("\n=== Summary ===")
print(f"High Risk Servers: {high}")
print(f"Working Servers: {working}")
print(f"OK Servers: {ok}")
print(f"Critical Systems: {critical_system}")

print("=== End of the Original Program ===")



