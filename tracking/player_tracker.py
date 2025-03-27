# models/player_tracker.py
from ultralytics import YOLO
import cv2

class PlayerTracker:
    def __init__(self, model_path='yolov8n.pt'):  # You can train a custom model later
        self.model = YOLO(model_path)

    def track(self, frame):
        results = self.model(frame, verbose=False)[0]
        players = []

        for box in results.boxes:
            cls_id = int(box.cls[0])
            label = self.model.names[cls_id]
            if label in ['person']:  # Only track humans
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                players.append(((x1, y1), (x2, y2)))

        return players
