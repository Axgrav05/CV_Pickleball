# models/ball_tracker.py
import cv2
import numpy as np

class BallTracker:
    def __init__(self):
        self.prev_frame = None

    def track(self, frame):
        if self.prev_frame is None:
            self.prev_frame = frame
            return None

        diff = cv2.absdiff(self.prev_frame, frame)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
        thresh = cv2.dilate(thresh, None, iterations=2)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        ball_candidate = None
        min_area = 5
        max_area = 100

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if min_area < area < max_area:
                (x, y, w, h) = cv2.boundingRect(cnt)
                ball_candidate = (x + w // 2, y + h // 2)
                break

        self.prev_frame = frame
        return ball_candidate
