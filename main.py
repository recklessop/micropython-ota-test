import time

print("Running main application...")

while True:
    print("Device is operational with 3.0 code!")
    time.sleep(5)

# In main.py
with open("log.txt", "a") as log:
    log.write("Device started successfully.\n")
    log.write("Running main program...\n")
