import cv2
import numpy as np
import os

# 計算PSNR和SSIM
def psnr_ssim(img1, img2):
    # 計算PSNR:數字越高代表圖像品質越好，處理後的圖像與原圖之間的誤差越小
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    psnr = 20 * np.log10(PIXEL_MAX / np.sqrt(mse))
    
    # 計算SSIM:數字的範圍在-1到1之間，值越接近1代表處理後的圖像越接近原圖，也就是圖像品質越好
    k1, k2 = 0.01, 0.03
    L = 255.0
    C1 = (k1 * L) ** 2
    C2 = (k2 * L) ** 2
    mu1, mu2 = np.mean(img1), np.mean(img2)
    sigma1_sq, sigma2_sq = np.var(img1), np.var(img2)
    img1_1d, img2_1d = img1.flatten(), img2.flatten()
    sigma12 = np.cov(img1_1d, img2_1d)[0][1]
    ssim = ((2 * mu1 * mu2 + C1) * (2 * sigma12 + C2)) / ((mu1 ** 2 + mu2 ** 2 + C1) * (sigma1_sq + sigma2_sq + C2))
    
    return psnr, ssim

# 定義高斯濾波
def gaussian_blur(image):
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    return blurred

# 定義中值濾波
def median_blur(image):
    blurred = cv2.medianBlur(image, 5)
    return blurred

# 定義雙邊濾波
def bilateral_blur(image):
    blurred = cv2.bilateralFilter(image, 9, 75, 75)
    return blurred

# 讀取資料夾中所有圖片
folder_path = 'D:\\fisher\\output_data_14\\c14_processing_picture'
output_path = "D:\\fisher\\output_data_14\\c14_filter_picture"
image_list = os.listdir(folder_path)

# 對每張圖片做高斯濾波，並計算PSNR和SSIM
choose = input("1 for gaussian, 2 for median, 3 for bilateral: ")
print("start filter..")
for image_name in image_list:
    # 讀取圖片
    image_path = os.path.join(folder_path, image_name)
    image = cv2.imread(image_path)
    
    # 做濾波
    if choose == '1':
        blurred = gaussian_blur(image)
    elif choose == '2':
        blurred = median_blur(image)
    elif choose == '3':  
        blurred = bilateral_blur(image)

    output_image_path = os.path.join(output_path, image_name)
    cv2.imwrite(output_image_path, blurred)

    # 計算PSNR和SSIM
    # psnr, ssim = psnr_ssim(image, blurred)
    
    # 輸出結果
    # print(f'{image_name}: PSNR={psnr}, SSIM={ssim}')
print("finish..")