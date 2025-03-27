### visualizations/metrics.py
import csv
from config.constants import FRAME_WIDTH, FRAME_HEIGHT, COURT_LENGTH, KITCHEN_LENGTH
from utils.tracking_utils import euclidean_distance

class Metrics:
    def __init__(self):
        self.data = []
        self.rally_count = 0
        self.prev_ball_pos = None
        self.kitchen_violations = 0

    def update(self, players, ball):
        self.data.append((players, ball))

        # Count rallies (ball motion)
        if self.prev_ball_pos is not None and ball is not None:
            dist = euclidean_distance(ball, self.prev_ball_pos)
            if dist > 10:
                self.rally_count += 1

        self.prev_ball_pos = ball

        # Kitchen violation check (simple vertical zone check)
        if players:
            for (tl, br) in players:
                cx = (tl[0] + br[0]) // 2
                cy = (tl[1] + br[1]) // 2
                y_mapped = (cy / FRAME_HEIGHT) * COURT_LENGTH
                court_center = COURT_LENGTH / 2
                in_kitchen = abs(y_mapped - court_center) < KITCHEN_LENGTH
                if in_kitchen:
                    self.kitchen_violations += 1

    def export(self):
        with open("output_videos/metrics.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Frame", "Player Count", "Ball X", "Ball Y"])
            for i, (players, ball) in enumerate(self.data):
                bx, by = ball if ball else ("", "")
                writer.writerow([i, len(players), bx, by])

        with open("output_videos/summary.txt", "w") as f:
            f.write(f"Total Frames: {len(self.data)}\n")
            f.write(f"Rally Count (est.): {self.rally_count}\n")
            f.write(f"Kitchen Violations (est.): {self.kitchen_violations}\n")