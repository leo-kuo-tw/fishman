import cv2
import os

video_path = 'D:\\fisher\\Camera14\\'
output_pic_path = 'D:\\fisher\\output_data_14\\c14_origin_picture'
avi_files_list = [f for f in os.listdir(video_path) if f.endswith('.avi')]
count = 1

for avi in avi_files_list:
    file_path = os.path.join(video_path, avi)
    video = cv2.VideoCapture(file_path)
    # fps是影片的幀率，表示每秒鐘顯示的影格數量
    fps = video.get(cv2.CAP_PROP_FPS)
    # 影片總共的幀數是影片中包含的所有幀的數量
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    time = 0
    # 影片名稱長度固定
    name = avi[:17]

    if not video.isOpened():
        print("avi開啟失敗")
        exit()
    print(avi + " running..")

    while video.isOpened():
        video.set(cv2.CAP_PROP_POS_MSEC, time)
        ret, frame = video.read()

        if not ret:
            break

        output_name = os.path.join(output_pic_path, name + '_' + str(count) + '.png')
        cv2.imwrite(output_name, frame)

        count+=1
        # 時間以毫秒為單位，1 min 一張
        time += 60000

        if time >= frame_count / fps * 1000:
            break
    print(avi + " finish")
    video.release()