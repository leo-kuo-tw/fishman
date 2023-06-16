import cv2
import os

picture_path = "D:\\fisher\\output_data_14\\c14_origin_picture"
output_path = "D:\\fisher\\output_data_14\\c14_processing_picture"

def data_resize(name):
    print("start resize..")
    for n in name:
        data = os.path.join(picture_path, n)
        img = cv2.imread(data)
        re_img = cv2.resize(img, (640, 640))
        cv2.imwrite(os.path.join(output_path, n), re_img)
    print("finish..")

def data_cut(name):
    print("start cutting..")
    for n in name:
        data = os.path.join(picture_path, n)
        img = cv2.imread(data)
        width = img.shape[1]
        crop_width = int(width * 0.3)
        cropped_img = img[:, crop_width:]
        cv2.imwrite(data, cropped_img)
    data_resize(name)

if __name__ == "__main__":
    picture_name = [f for f in os.listdir(picture_path) if f.endswith(".png")]
    data_cut(picture_name)