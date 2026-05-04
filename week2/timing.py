import time

start = time.time()

for i in range(100):
    time.sleep(.01)

for i in range(100):
    time.sleep(.01)

end = time.time()

print(end-start)