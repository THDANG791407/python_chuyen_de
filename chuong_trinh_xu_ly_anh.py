import cv2
import os
import numpy as np

def get_output_path(image_path, suffix):
    folder = os.path.dirname(image_path)
    filename = os.path.basename(image_path)
    name, ext = os.path.splitext(filename)
    return os.path.join(folder, f"{name}_{suffix}{ext}")

def compress_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Lỗi: Không thể mở ảnh. Hãy kiểm tra đường dẫn!")
        return
    compressed = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2), interpolation=cv2.INTER_AREA)
    output_path = get_output_path(image_path, "compressed")
    cv2.imwrite(output_path, compressed)
    print(f"Ảnh đã được lưu tại: {output_path}")
    cv2.imshow("Compressed Image", compressed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def blur_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Lỗi: Không thể mở ảnh. Hãy kiểm tra đường dẫn!")
        return
    blurred = cv2.GaussianBlur(image, (15, 15), 0)
    output_path = get_output_path(image_path, "blurred")
    cv2.imwrite(output_path, blurred)
    print(f"Ảnh đã được lưu tại: {output_path}")
    cv2.imshow("Blurred Image", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def convert_to_grayscale(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Lỗi: Không thể mở ảnh. Hãy kiểm tra đường dẫn!")
        return
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    output_path = get_output_path(image_path, "grayscale")
    cv2.imwrite(output_path, gray)
    print(f"Ảnh đã được lưu tại: {output_path}")
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def sobel_edge_detection(image_path):
    image = cv2.imread(image_path, 0)
    if image is None:
        print("Lỗi: Không thể mở ảnh. Hãy kiểm tra đường dẫn!")
        return
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.magnitude(sobel_x, sobel_y)
    output_path = get_output_path(image_path, "sobel")
    cv2.imwrite(output_path, sobel.astype(np.uint8))
    print(f"Ảnh đã được lưu tại: {output_path}")
    cv2.imshow("Sobel Edge Detection", sobel.astype(np.uint8))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    image_path = input("Nhập đường dẫn ảnh: ").replace("\\", "/")  # Nhập 1 lần để sử dụng lại
    
    while True:
        print("\n" + "*" * 40)
        print("\n        CHƯƠNG TRÌNH XỬ LÝ ẢNH\n")
        print("*" * 40)
        print("1. Nén ảnh")
        print("2. Làm mờ ảnh")
        print("3. Chuyển ảnh màu sang ảnh xám")
        print("4. Phát hiện biên cạnh bằng Sobel")
        print("5. Thoát chương trình")
        print("*" * 40)

        choice = input("Chọn thuật toán (1-5): ")

        if choice == "1":
            compress_image(image_path)
        elif choice == "2":
            blur_image(image_path)
        elif choice == "3":
            convert_to_grayscale(image_path)
        elif choice == "4":
            sobel_edge_detection(image_path)
        elif choice == "5":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    main()
