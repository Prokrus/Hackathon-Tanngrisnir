import cv2
import tkinter as tk
from PIL import Image, ImageTk
import time
import threading
import logger as log
import veh_data
import random
import queue

VIDEO_PATH = '../../Driving_in_London.mp4'
TIME_FEATURE_0 = 10 # sec features inquire
TIME_FEATURE_1 = 20 # sec high incar_temperature
TIME_FEATURE_2 = 45 # sec quiet vehicle & local life suggestion
TIME_FEATURE_3 = 80 # sec traffic light Red-to-green reminder
TIME_FEATURE_4 = 85 # sec Fatigue Relief

queue = queue.Queue()
# video play time to get feature
play_time = 0
logger = log.Logger()

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

    root = tk.Tk()
    root.withdraw()
    logger.show_logger(root)
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

        logger.print_logger()
          # quit window
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    # close window and video
    video.release()
    cv2.destroyAllWindows()
    # run
    window.mainloop()
    root.mainloop()

def monitor_time():
    global play_time
    data = veh_data.VehData()
    while True:
        print("Currently Video Time：{:.1f} Sec".format(play_time))
        time.sleep(1)

        if int(play_time) >= TIME_FEATURE_0 and int(play_time) < TIME_FEATURE_1:
            print("feature0")
            # doing something
            data.setData(1,
                         random.randint(23, 25),
                         True,
                         True,
                         random.randint(1, 3),
                         False,
                         False,
                         random.random() < 0.5,
                         random.random(),
                         random.randint(80, 81),
                         2,
                         True,
                         True,
                         random.randint(30, 35),
                         False,
                         False)

        elif int(play_time) >= TIME_FEATURE_0 and int(play_time) < TIME_FEATURE_1:
            print("feature1")
            # doing something
            data.setData(2,
                         random.randint(23, 25),
                         True,
                         False,
                         random.randint(1, 3),
                         False,
                         False,
                         random.random() < 0.5,
                         random.random(),
                         random.randint(80, 81),
                         2,
                         True,
                         True,
                         random.randint(30, 35),
                         False,
                         False)

        elif int(play_time) >= TIME_FEATURE_2 and int(play_time) < TIME_FEATURE_3:
            print("feature2")
            # doing something
            data.setData(3,
                         random.randint(23, 25),
                         True,
                         False,
                         random.randint(1, 3),
                         True,
                         False,
                         random.random() < 0.5,
                         random.random(),
                         random.randint(80, 81),
                         0,
                         False,
                         False,
                         0,
                         False,
                         True)

        elif int(play_time) >= TIME_FEATURE_3 and int(play_time) < 85:
            print("feature3")
            # doing something
            data.setData(4,
                         random.randint(23, 25),
                         True,
                         False,
                         random.randint(1, 3),
                         False,
                         False,
                         random.random() < 0.5,
                         random.random(),
                         random.randint(80, 81),
                         2,
                         True,
                         True,
                         0,
                         False,
                         False)

        elif int(play_time) >= TIME_FEATURE_4 and int(play_time) < 100:
            print("feature4")
            # doing something
            data.setData(5,
                         random.randint(23, 25),
                         True,
                         False,
                         random.randint(1, 3),
                         False,
                         False,
                         random.random() < 0.5,
                         random.random(),
                         random.randint(80, 81),
                         0,
                         False,
                         False,
                         random.randint(20, 25),
                         True,
                         False)
        elif int(play_time) < TIME_FEATURE_1:
            # generate random data
            data.setData(0,
                         33,
                         True,
                         False,
                         random.randint(1, 3),
                         False,
                         False,
                         random.random() < 0.5,
                         random.random(),
                         random.randint(80, 81),
                         0,
                         True,
                         True,
                         random.randint(30, 35),
                         False,
                         False)
        else:
            data.setData(6,
                         33,
                         True,
                         False,
                         random.randint(1, 3),
                         False,
                         False,
                         random.random() < 0.5,
                         random.random(),
                         random.randint(80, 81),
                         0,
                         True,
                         True,
                         random.randint(30, 35),
                         False,
                         False)
        logger.set_logger(data)

def run():
    t1 = threading.Thread(target=monitor_time)
    t1.start()
    play_video()

if __name__ == '__main__':
    run()
