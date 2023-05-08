import cv2
import numpy as np
from calOptical import calOptical
from clickPos import clickPos
import getFreq
videoFilePath = "/Users/lijianhao/Desktop/test.mp4"
videoOutputPath = "/Users/lijianhao/Desktop/result.mp4"
SAVE_VIDEO = True

def main():
    #process videos into pictures
    
    cap = cv2.VideoCapture(videoFilePath)
    ret, prev = cap.read()

    # Check if the frame was successfully read
    if not ret:
        print("fail to load the video")
        return 0
    print("video loaded")
    
    # set the pos you want to track
    cv2.namedWindow("image",0)
    p0 = np.array(clickPos(prev))
    
    paths = []
    paths.append(p0)
    
    # Define the codec and create VideoWriter object
    
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    
    out = cv2.VideoWriter()
    success = out.open(videoOutputPath,fourcc, 20.0, (1280,720),True)
    
    if not success:
        print("fail to save the video")
    
    while cap.isOpened():
        # Read the next frame
        ret, cur = cap.read()
    
        # Check if the frame was successfully read
        if not ret:
            break
    
        # Process the frame here...
    
        # Display the current frame
        calOptical(prev, cur, paths[-1], paths)
        
        cv2.imshow('image', cur)
        prev = cur
        
        out.write(cur)
        
        # Check if the user pressed 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    # Release the video capture object and close all windows
    
    getFreq.plotFreq(paths)
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    
    return

if __name__=="__main__":
    main()
            
    
