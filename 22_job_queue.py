import os, time, random, queue, threading

# create the file list
photo_folder = r"D:\Work\_PythonSuli\kezdo-230304\photos"
files = os.listdir(photo_folder)

# create a job queue
job_queue = queue.Queue()
for f in files:
    job_queue.put(f)


def worker():
    while not job_queue.empty():
        file = job_queue.get()
        print(f"Working on: {file}...")
        time.sleep(random.randint(1, 10))
        print("Work finished.")
        job_queue.task_done()
    
t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)
t3 = threading.Thread(target=worker)
t4 = threading.Thread(target=worker)

for _ in range(8):
    t = threading.Thread(target=worker)
    t.start()