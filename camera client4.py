"""
Color detection application using OpenCV and Tkinter.
"""

import tkinter as tk
from PIL import Image, ImageTk
import cv2  # pylint: disable=import-error
import numpy as np


class ColorDetectionApp:
    """Color detection application using OpenCV and Tkinter."""

    def __init__(self, root):
        """Initialize the application."""
        self.root = root
        self.root.title("Color Detection")
        self.root.geometry("800x600")

        self.camera = None
        self.video_source = 0
        self.video_playing = False

        self.lower_color = np.array([30, 50, 50])
        self.upper_color = np.array([90, 255, 255])

        self.create_widgets()
        self.open_camera()
        self.update()

    def create_widgets(self):
        """Create and place UI widgets."""
        self.canvas = tk.Canvas(self.root, width=640, height=480)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        input_frame = tk.Frame(self.root)
        input_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.start_stop_button = tk.Button(input_frame, text="Start", command=self.start_stop)
        self.start_stop_button.pack(side=tk.LEFT, padx=10, pady=10)

        source_label = tk.Label(input_frame, text="Select Input Source:")
        source_label.pack(side=tk.LEFT, padx=10, pady=10)

        self.source_var = tk.StringVar()
        self.source_var.set("Webcam")

        source_option_menu = tk.OptionMenu(input_frame, self.source_var, "Webcam", "HDMI", "USB", "URL", command=self.change_source)
        source_option_menu.pack(side=tk.LEFT, padx=10, pady=10)

        self.url_entry = tk.Entry(input_frame)
        self.url_entry.pack(side=tk.LEFT, padx=10, pady=10)
        self.url_entry.insert(0, "http://192.168.1.101:8000/stream.mjpg")

        self.lower_hue = tk.Scale(input_frame, from_=0, to=180, orient=tk.HORIZONTAL, label="Lower Hue", command=self.update_color)
        self.lower_hue.set(30)
        self.lower_hue.pack(side=tk.LEFT, padx=10, pady=10)

        self.upper_hue = tk.Scale(input_frame, from_=0, to=180, orient=tk.HORIZONTAL, label="Upper Hue", command=self.update_color)
        self.upper_hue.set(90)
        self.upper_hue.pack(side=tk.LEFT, padx=10, pady=10)

        self.color_stats_label = tk.Label(input_frame, text="")
        self.color_stats_label.pack(side=tk.RIGHT, padx=10, pady=10)

        self.root.bind("<Control-s>", lambda event: self.start_stop())

    def change_source(self, source):
        """Change the video source."""
        if source == "Webcam":
            self.video_source = 0
        elif source == "HDMI":
            self.video_source = 1
        elif source == "USB":
            self.video_source = 2
        elif source == "URL":
            self.video_source = self.url_entry.get()
        self.open_camera()

    def open_camera(self):
        """Open the camera based on the selected source."""
        if isinstance(self.video_source, int):
            self.camera = cv2.VideoCapture(self.video_source, cv2.CAP_DSHOW)  # pylint: disable=no-member
        else:
            self.camera = cv2.VideoCapture(self.video_source)  # pylint: disable=no-member

        if not self.camera.isOpened():
            print(f"Error: Unable to open video source {self.video_source}")
        else:
            print(f"Video source {self.video_source} opened successfully")
            width = self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)  # pylint: disable=no-member
            height = self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)  # pylint: disable=no-member
            fps = self.camera.get(cv2.CAP_PROP_FPS)  # pylint: disable=no-member
            print(f"Video properties: Width={width}, Height={height}, FPS={fps}")

    def start_stop(self):
        """Toggle video playback."""
        if self.video_playing:
            self.video_playing = False
            self.start_stop_button.config(text="Start")
        else:
            self.video_playing = True
            self.start_stop_button.config(text="Stop")

    def update_color(self, _value):
        """Update the color detection range."""
        self.lower_color[0] = self.lower_hue.get()
        self.upper_color[0] = self.upper_hue.get()

    def detect_color(self, frame):
        """Detect a specific color in the frame."""
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # pylint: disable=no-member
        mask = cv2.inRange(hsv, self.lower_color, self.upper_color)  # pylint: disable=no-member
        res = cv2.bitwise_and(frame, frame, mask=mask)  # pylint: disable=no-member
        return res

    def update(self):
        """Continuously update the video frame and statistics."""
        if self.video_playing:
            ret, frame = self.camera.read()
            if ret:
                frame_with_color = self.detect_color(frame)
                frame_with_color = cv2.cvtColor(frame_with_color, cv2.COLOR_BGR2RGB)  # pylint: disable=no-member
                img = Image.fromarray(frame_with_color)

                canvas_width = self.canvas.winfo_width()
                canvas_height = self.canvas.winfo_height()
                img = img.resize((canvas_width, canvas_height), Image.BILINEAR)

                img_tk = ImageTk.PhotoImage(image=img)
                self.canvas.img_tk = img_tk
                self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)

                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # pylint: disable=no-member
                mask = cv2.inRange(hsv, self.lower_color, self.upper_color)  # pylint: disable=no-member
                pixel_count = cv2.countNonZero(mask)
                frame_area = frame.shape[0] * frame.shape[1]
                color_coverage_percentage = (pixel_count / frame_area) * 100

                if pixel_count > 0:
                    M = cv2.moments(mask)  # pylint: disable=invalid-name
                    centroid_x = int(M["m10"] / M["m00"])
                    centroid_y = int(M["m01"] / M["m00"])
                else:
                    centroid_x = centroid_y = 0

                self.color_stats_label.config(
                    text=f"Pixels Detected: {pixel_count}\n"
                         f"Centroid: ({centroid_x}, {centroid_y})\n"
                         f"Color Coverage: {color_coverage_percentage:.2f}%"
                )

        self.root.after(10, self.update)

    def run(self):
        """Run the Tkinter main loop."""
        self.root.mainloop()


if __name__ == "__main__":
    root_window = tk.Tk()
    app = ColorDetectionApp(root_window)
    app.run()
