from time import time

class StreamObj():
    def __init__(self):
        self.frames = [open('app/static/imageSeq/rancor_GL_jpg/rancorGL0' + str(n) + '.jpg',
                'rb').read() for n in range(210,270)]
    
    def getStreamf(self):
        return self.frames[int(time()) % 60]
        