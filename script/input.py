import cv2
import tkinter as tk
from PIL import Image, ImageTk
import time
import threading

VIDEO_PATH = '../../NIO_ET7_20230222_1329_Parking_To_Road.MOV'
TIME_FEATURE_0 = 1 # sec
TIME_FEATURE_1 = 2 # sec
TIME_FEATURE_2 = 3 # sec
TIME_FEATURE_3 = 4 # sec
TIME_FEATURE_4 = 5 # sec

# video play time to get feature
play_time = 0
def play_video():
    global play_time
    # open video file
    video = cv2.VideoCapture(VIDEO_PATH)
    fps = video.get(cv2.CAP_PROP_FPS)
    # get width of video
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    # get height of video
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # create window
    window = tk.Tk()
    window.title("Video Tool")
    str_size = str(int(width)) + "x" + str(int(height))
    window.geometry(str_size)
    print("video size: ", str_size)
    # create canvas
    canvas = tk.Canvas(window, width=width, height=height)
    canvas.pack()
    # get video and show it on canvas
    while True:
        ret, frame = video.read()
        if not ret:
            break
        # OpenCV to PIL
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        # 将PIL to ImageTk
        photo = ImageTk.PhotoImage(image)
        # show image on canvas
        canvas.create_image(0, 0, image=photo, anchor=tk.NW)
        # update window
        window.update()
        # cal video play time
        play_time += 1 / fps
        delay = int(1000 / fps)
        # quit window
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    # close window and video
    video.release()
    cv2.destroyAllWindows()
    # run
    window.mainloop()

def monitor_time():
    global play_time
    while True:
        print("Currently Video Time：{:.1f} Sec".format(play_time))
        time.sleep(1)
        if int(play_time) == TIME_FEATURE_0:
            print("feature0")
            # doing something and logger

        elif int(play_time) == TIME_FEATURE_1:
            print("feature1")
            # doing something and logger

        elif int(play_time) == TIME_FEATURE_2:
            print("feature2")
            # doing something and logger

        elif int(play_time) == TIME_FEATURE_3:
            print("feature3")
            # doing something and logger

        elif int(play_time) == TIME_FEATURE_4:
            print("feature4")
            # doing something and logger


def run():
    t1 = threading.Thread(target=play_video)
    t2 = threading.Thread(target=monitor_time)
    t1.start()
    t2.start()

if __name__ == '__main__':
    print('Inputing...')
    run()
    print('finish')