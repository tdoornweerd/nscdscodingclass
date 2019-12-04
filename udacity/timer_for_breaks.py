import time
import webbrowser
for i in range(10):
    print('this program started at' + time.ctime())
    time.sleep(5)#in seconds 
    webbrowser.open('https://www.youtube.com/watch?v=d7mrBC0zLZg')

print('done')