# Civil-Engineering_movement_tracking

https://github.com/shinkiriu/Civil-Engineering_movement_tracking

This project is meant to track the pixel movement of positions in a video and reflect its frequency. We used [LK optical flow](https://en.wikipedia.org/wiki/Lucas%E2%80%93Kanade_method) method to track the pos movement between frames.

## Environments
  * OpenCV 4.6.0

  * Python 3.8.16

  * Numpy 1.23.5

## Steps to run
  * Change the video input and output path in main.py

  * Run main.py, select the positions you want to track on opencv image, press q to quit.

## Result
<img width="427" alt="image" src="https://user-images.githubusercontent.com/48248780/236725362-e044137f-2223-44c6-bce4-8578ce000a82.png">

Straight forward, [This video](https://drive.google.com/file/d/1rrRuoTUt3h_J-Hxvn1xNl_YyTGtmjJWK/view?usp=sharing) show the movement of positions we selected.
