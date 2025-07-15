import time
 
countdown = 10
start_time = time.time()
elapsed_time = 0
  
while (remaining_time := countdown - elapsed_time) > 0:
  
    print(f"Countdown: {int(remaining_time)} seconds remaining")
    time.sleep(1)  # wait for 1 second
    elapsed_time = time.time() - start_time
else:
    print("Time's up!")
