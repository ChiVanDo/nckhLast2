import cv2
import numpy as np
import os

def save(img, img_counter):
    
    imgName = "{}.jpg".format(img_counter)
    output_path = f"{'SaveImage/p'}/{imgName}" # lưu ảnh vào đường link img với imgName là tên
    cv2.imwrite(output_path, img)
    print("{}writen!".format(imgName))  

def main():
    cam = cv2.VideoCapture(1)
    img_counter = 1
    while True:
        _, image = cam.read()
        
        cv2.imshow("images", image)
        k = cv2.waitKey(1)
        
        
        if k % 256 == 32:
            img_counter = img_counter + 1
            save(image, img_counter)
        elif k % 256 == 27:
            print("Close")
            break

def reziseImage():
    #  for i in range(1, 23):  # Từ 1 đến 22
    #     image_filename = os.path.join('SaveImage/p', f'{i}.jpg')
        
    #     # Kiểm tra xem tệp ảnh tồn tại không
    #     if os.path.exists(image_filename):
    #         # Đọc ảnh sử dụng OpenCV
    #         image = cv2.imread(image_filename)
            
    #         # Hiển thị ảnh
    #         cv2.imshow(f'Image {i}', image)
    for i in range(1,26):
        image_filename = os.path.join('SaveImage/p', f'{i}.jpg')
        
        # Kiểm tra xem tệp ảnh tồn tại không
        if os.path.exists(image_filename):
            # Đọc ảnh sử dụng OpenCV
            image = cv2.imread(image_filename)
            
            image = cv2.resize(image, (350,350))
            
            save(image, i)
            # Hiển thị ảnh
            #cv2.imshow(f'Image {i}', image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    #main()
    reziseImage()
