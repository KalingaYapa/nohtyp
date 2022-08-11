

from operator import imod
import requests
#from threading import Thread
from multiprocessing import Process


class ImageDownloaderThread(Process) : 
    
    def __init__(self, thread_id, name, urls, success_count) -> None:
        super(ImageDownloaderThread,self).__init__()
        self.thread_id = thread_id
        self.name = name
        self.urls = urls
        self.success_count = success_count

    def run(self) -> None:
        count = 0
        for i,url in enumerate(self.urls) :
            if self.download_image(url,f'{self.thread_id}-{i}') : 
                count += 1
        
        self.success_count.put(count)
       
    def download_image(self ,url , image_number) :
        response = requests.get(url=url, stream=True)
        if response.status_code == 200 :
            file_name = f'images/{image_number}.jpg'
            with open(file_name, "wb") as f:
                f.write(response.content)

            print('Images Successfully Downloaded',file_name)
            return True    
        else :
            print('Images Couldn\'t Downloaded')
            return False