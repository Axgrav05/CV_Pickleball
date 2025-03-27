### utils/draw_utils.py
import cv2

def draw_overlays(frame, players, ball):
    for (top_left, bottom_right) in players:
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

    if ball is not None:
        cv2.circle(frame, ball, 5, (0, 0, 255), -1)

    return frame