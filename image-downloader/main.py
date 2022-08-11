#https://picsum.photos/id/237/200/300
import time
import my_thread
from queue import Queue

def get_image_url(count) :

    if count <= 0:
        print("Invalid Count")
        return
    
    for i in range (0,count):
        url = f'https://picsum.photos/id/{i}/800/1600'
        yield url 

urls = list(get_image_url(100))
new_urls = []
num_threads = 10
success_count = Queue()

# Url list splitted to sub arrays
for i in range(0,len(urls),num_threads) : 
    list = urls[i:i + num_threads]
    new_urls.append(list)

start = time.time_ns()
threads = []

count = 0
for i,urls in enumerate(new_urls) : 
    thread = my_thread.ImageDownloaderThread(i, f'Thread-{i}', urls, success_count)
    thread.start()
    threads.append(thread)

#Main thread waits here until complete all the running threads
for thread in threads : 
    thread.join()

for i in range(num_threads):
    count += success_count.get()

duration = time.time_ns() - start
print(f'{count} Images Successfully Downloaded  Within {duration/1000000} ms ')