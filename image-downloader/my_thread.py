

import requests
from threading import Thread


class ImageDownloaderThread(Thread) : 
    
    def __init__(self, thread_id, name, urls) -> None:
        super(ImageDownloaderThread,self).__init__()
        self.thread_id = thread_id
        self.name = name
        self.urls = urls

    def run(self) -> None:
        for i,url in enumerate(self.urls) :
            self.download_image(url,f'{self.thread_id}-{i}')
       
    def download_image(self ,url , image_number) :
        response = requests.get(url=url, stream=True)
        if response.status_code == 200 :
            file_name = f'images/{image_number}.jpg'
            with open(file_name, "wb") as f:
                f.write(response.content)

            print('Images Successfully Downloaded',file_name)    
        else :
            print('Images Couldn\'t Downloaded')