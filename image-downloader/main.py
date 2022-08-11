#https://picsum.photos/id/237/200/300
import time
import my_thread

def get_image_url(count) :

    if count <= 0:
        print("Invalid Count")
        return
    
    for i in range (0,count):
        url = f'https://picsum.photos/id/{i}/800/1600'
        yield url 

urls = list(get_image_url(100))
new_urls = []
num_threds = 10

# Url list splited to sub arrays
for i in range(0,len(urls),num_threds) : 
    list = urls[i:i + num_threds]
    new_urls.append(list)

start = time.time_ns()
threads = []

for i,urls in enumerate(new_urls) : 
    thread = my_thread.ImageDownloaderThread(i, f'Thread-{i}', urls)
    thread.start()
    threads.append(thread)

#Main thread waits here untill complete all the started threads
for thread in threads : 
    thread.join()

duration = time.time_ns() - start
print('Total Duration in ms' , duration/1000000)