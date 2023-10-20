import cv2
import numpy as np




def save(img, img_counter):
    imgName = "{}.jpg".format(img_counter)
    output_path = f"{'SaveImage/p'}/{imgName}" # lưu ảnh vào đường link img với imgName là tên
    cv2.imwrite(output_path, img)
    print("{}writen!".format(imgName))  
    
def confrim(image):
    image = cv2.GaussianBlur(image, (15,15),0)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Xác định ngưỡng cho màu trắng trong không gian màu HSV
    lower = np.array([10, 100, 200]) # [màu,  độ bão hòa, độ sáng]
    upper = np.array([35, 255, 255])

        # Tạo mask để nhận biết màu trắng
    mask = cv2.inRange(hsv_image, lower, upper) # chuyển về ảnh nhị phân
    cv2.imshow("mask", mask)
        
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)   
        
        
    output = cv2.bitwise_and(image, hsv_image, mask= mask)
        
    vungSang = cv2.countNonZero(mask)
    if int(vungSang) > 1:
        print(vungSang)
            
            
    cv2.imshow("output", output)
    
    
def main():
    fire_cascade = cv2.CascadeClassifier('SaveImage/fire_detection.xml')
    cam = cv2.VideoCapture(0)
 
    sl = 1
    
    while True:
      
        _, image = cam.read()
       
        
        
        x, y, w, h = 0, 0, 0, 0
        # Áp dụng mask lên hình ảnh gốc

        fire = fire_cascade.detectMultiScale(image, 1.05, 3)
        for x, y, w, h in fire:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
            
        
        
        
        if(w != 0 or h != 0):
            sl = sl + 1
            x1 = x + w
            y1 = y + h
            cut = image[y - 10:y1 + 10 , x - 10:x1 + 10] # vùng cần check.
            confrim(cut)
        
        
            
        cv2.imshow("fr", image)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            print("Close")
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()