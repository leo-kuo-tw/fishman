# Are the fishermen in the video of oceanic fishing overworked or not
### Data provider: Taiwan Tuna Association
According to the rule of ILO, fishermen need a minimum period of rest not less than 10 hours in any 24-hour period and of 77 hours in any seven-day period, otherwise, it is overworked.    
The camera is located in the working area of the fishermen. The working hours of Camera13 and 14 are separated.
## Dataset
### Raw data
There have 94 videos in avi format.
* Camera13: 41.8G, 63 files.
* Camera14: 20.8G, 31 files.

**Due to intellectual property, data can't be published.**

### Video to image
Capture a screenshot of the video per minute, you can modify the interval time in video_cut.py
* Camera13: 15G, 7394 files (.png), 1920*1080.
* Camera14: 7.3G, 3665 files (.png), 1920*1080.

### Data preprocessing
According to observation, there are few people on the left side of the video, and we want to adjust the input size to match yolo v7.  
In preprocess.py, you can modify the range of cutting size and resize.  
In img_filter.py, you can choose the type of filter.
* Crop 30% of the left side of the image, size becomes 1344*1080.
* Resize all the images to 640*640. (Resizing the image may introduce some noise)
* Gaussian filter, decreases the noise of the image and size of the image.
* Camera13: 4.1G, Camera14: 1.4G.  

## Label
Amount of images. Camera13 : Camera14 = 2520 : 1080 = 7 : 3, 1.6G
* Train: 2880
* Valid: 360
* Test: 360

Standard:
* People in white light.
* Upper body. (Machine covers the lower body)
* Select the most complete person shape in the overlapping crowd.
* We don't need the body blocked by objects.

## Train
Train on Google colab, use yolo v7 as pre-train model, weight is yolo v7.  
batch size: 16, epochs: 100  
yolo v7: https://github.com/WongKinYiu/yolov7  

## Detect
Modify detect.py in yolo v7, and add some conditions:
* Fps of videos are 30, 30 frames as 1 sec.
* If there is one fisherman appearing in Camera, it indicates working time, and everyone is working.
* If the parameter "pred" is empty and more than 15 frames are detected within one second, it indicates the fishermen are working during that second.
* Calculate the total number that satisfies the condition and output it as a txt file. By summing up the numbers, we can determine the total working hours and determine whether the fishermen are overworked.

Detail code: https://colab.research.google.com/drive/1P8j4QBM1N59Byuxv0FPJttVtN7CS7KHT?usp=drive_link  
## Challenge
* Because it is difficult to accurately identify the faces of fishermen and their attire changes daily, it can't detect if a specific fisherman is working longer hours than others.
  * Try to use skeleton detection model to identify each fisherman.
* It takes more than one hour to run the detection on colab for a 2 hours video, which results in a long detection time.
  * Stronger hardware

## Conclusion
* Transform the large raw data into images that are suitable for training on colab.
* The performance of YOLO v7 is good, as it can accurately detect the majority of fishermen.
* Calculate the working hours and check if the fishermen are overworked or not.

Project ppt: https://docs.google.com/presentation/d/1MITeXN5LBp1QtxZg3FOwQDmGof3KKNSj/edit?usp=sharing&ouid=102983354699040806655&rtpof=true&sd=true
***

# 遠洋漁業的漁工影像中是否過勞
### 資料提供者: 台灣鮪魚公會
根據國際勞動組織(ILO)規定，漁工一天內至少要休息10小時，且一周內要休息至少77小時，否則就算過勞，檢測公會提供的影片，看是否有過勞的情況。     
Camera的拍攝地點是漁工的作業區，Camera13與14的漁工上班時間是分開的。
## Dataset
### Raw data
共有94個影片，為avi檔。
* Camera13: 41.8G, 63 files。
* Camera14: 20.8G, 31 files。

**因為智慧財產權，資料無法公開。**

### Video to image
影片每一分鐘做一次截圖，可在video_cut.py中修改間隔時間。
* Camera13: 15G, 7394 files (.png), 1920*1080。
* Camera14: 7.3G, 3665 files (.png), 1920*1080。

### Data preprocessing
根據觀察，影片左半邊不常有人，且為了符合yolo v7的input大小。  
在preprocess.py中，修改切除範圍與resize大小。  
在img_filter.py中，可以選擇filter的類型。
* 切除圖片左邊的30%，size變成1344*1080。
* Resize所有圖片成640*640。 (調整影像大小可能會導致一些噪聲)
* 做Gaussian filter，減少圖片中的噪聲，也可以降低圖片size。
* Camera13: 4.1G, Camera14: 1.4G。  

## Label
數量 Camera13 : Camera14 = 2520 : 1080 = 7 : 3, 1.6G
* Train: 2880
* Valid: 360
* Test: 360

標準:
* 白光中的人影。
* 上半身。 (下半身有機台阻擋)
* 重疊人群中，選人型最完整的。
* 身體被物體遮擋者，不需要。

## Train
在Google colab做訓練，使用yolo v7作為預模型，權重為yolo v7。  
batch size: 16, epochs: 100  
yolo v7: https://github.com/WongKinYiu/yolov7  

## Detect
修改yolo v7中的detect.py，加入條件:
* 影片fps為30，設定30幀為1秒。
* 只要有一位漁工出現在Camera中，代表是上班時間，全員都在上班。
* 判斷預測參數pred是否為空，且一秒內超過15幀被偵測到，代表這一秒有漁工在工作。
* 計算符合條件的總數，並輸出成txt檔，將其加總後，得到總工時，就可知道是否過勞。

詳細程式碼修改: https://colab.research.google.com/drive/1P8j4QBM1N59Byuxv0FPJttVtN7CS7KHT?usp=drive_link  
## Challenge
* 因為無法清楚辨識影片中漁工的臉部，每天的穿著也不同，無法針對每個人做label，無法檢測是否有特定漁工工時特別長。
  * 可嘗試用骨架辨識模型找出每個漁工。
* Detect一個2小時的影片，在colab上需要執行1個多小時，檢測時間過長。
  * 加強硬體設備。

## Conclusion
* 將龐大的raw data轉換成適合訓練的image，且大小不會超過colab限制。
* yolo v7表現良好，能找出大部分漁工。
* 計算工時，檢查是否過勞。

專案簡報: https://docs.google.com/presentation/d/1MITeXN5LBp1QtxZg3FOwQDmGof3KKNSj/edit?usp=sharing&ouid=102983354699040806655&rtpof=true&sd=true
