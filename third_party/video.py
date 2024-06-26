import cv2

# 树莓派的IP地址和Motion提供的视频流端口
raspberry_pi_ip = "192.168.0.30"
stream_port = 8081

# 构建视频流URL
stream_url = f"http://{raspberry_pi_ip}:{stream_port}"

# 打开视频流
cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("无法打开视频流")
    exit()

# 读取并显示视频流
while True:
    ret, frame = cap.read()
    if not ret:
        print("无法接收视频帧")
        break

    cv2.imshow('Video Stream', frame)

    # 按 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
