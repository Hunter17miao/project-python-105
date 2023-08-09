import os
import cv2


path = "/Users/huntermiao/Desktop/Project105/PRO-C105-Project-Images-main/Images"


Images = []


for file in os.listdir(path):
    name, extension = os.path.splitext(file)
    

    if ext in ['.jpg', '.jpeg', '.png']:
        file_name = path+"/"+name


count = len(Images)


frame = cv2.imread(Images[0])
height, width, channels = frame.shape
size = (width, height)


out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)


for i in range(count):
    img = cv2.imread(Images[i])
    out.write(img)


out.release()

print("Done")