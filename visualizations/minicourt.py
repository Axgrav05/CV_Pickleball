### visualizations/minicourt.py
import numpy as np
import cv2
from config.constants import MINICOURT_WIDTH, MINICOURT_HEIGHT

class MiniCourt:
    def __init__(self):
        self.frame = np.ones((MINICOURT_HEIGHT, MINICOURT_WIDTH, 3), dtype=np.uint8) * 255

    def update(self, players, ball):
        self.frame[:] = 255  # Clear court
        # Draw court lines
        cv2.rectangle(self.frame, (0, 0), (MINICOURT_WIDTH - 1, MINICOURT_HEIGHT - 1), (0, 0, 0), 2)
        mid_line = MINICOURT_HEIGHT // 2
        kitchen_offset = int((KITCHEN_LENGTH / COURT_LENGTH) * MINICOURT_HEIGHT)
        cv2.line(self.frame, (0, mid_line), (MINICOURT_WIDTH, mid_line), (0, 0, 0), 1)
        cv2.line(self.frame, (0, mid_line - kitchen_offset), (MINICOURT_WIDTH, mid_line - kitchen_offset), (200, 200, 200), 1)
        cv2.line(self.frame, (0, mid_line + kitchen_offset), (MINICOURT_WIDTH, mid_line + kitchen_offset), (200, 200, 200), 1)

        # Map players
        for (tl, br) in players:
            cx = (tl[0] + br[0]) // 2
            cy = (tl[1] + br[1]) // 2
            x = int((cx / FRAME_WIDTH) * MINICOURT_WIDTH)
            y = int((cy / FRAME_HEIGHT) * MINICOURT_HEIGHT)
            cv2.circle(self.frame, (x, y), 6, (0, 255, 0), -1)

        if ball is not None:
            bx = int((ball[0] / FRAME_WIDTH) * MINICOURT_WIDTH)
            by = int((ball[1] / FRAME_HEIGHT) * MINICOURT_HEIGHT)
            cv2.circle(self.frame, (bx, by), 4, (0, 0, 255), -1)

    def render(self):
        return self.frame.copy()