### main.py
import cv2
from config.constants import FRAME_WIDTH, FRAME_HEIGHT
from models.player_tracker import PlayerTracker
from models.ball_tracker import BallTracker
from utils.video_utils import load_video, save_video
from utils.draw_utils import draw_overlays
from visualizations.minicourt import MiniCourt
from visualizations.metrics import Metrics


def main():
    video_path = 'input_videos/sample.mp4'
    output_path = 'output_videos/annotated.mp4'

    frames = load_video(video_path)
    player_tracker = PlayerTracker()
    ball_tracker = BallTracker()
    minicourt = MiniCourt()
    metrics = Metrics()

    annotated_frames = []

    for frame in frames:
        players = player_tracker.track(frame)
        ball = ball_tracker.track(frame)

        frame = draw_overlays(frame, players, ball)
        minicourt.update(players, ball)
        metrics.update(players, ball)

        annotated_frames.append(frame)

    metrics.export()
    save_video(annotated_frames, output_path)


if __name__ == '__main__':
    main()
