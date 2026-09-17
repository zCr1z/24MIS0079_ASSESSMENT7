import time

print("Backend check started")

for i in range(1, 4):
    print(f"Backend working... {i}")
    time.sleep(1)

print("Backend checks passed.")