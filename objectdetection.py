from ultralytics import YOLO

model = YOLO("yolo11s.pt")

result = model.predict(source="0", show=True) #this code is use for open camera

print(result)