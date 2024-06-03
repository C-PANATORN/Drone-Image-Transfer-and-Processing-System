# Drone Image Transfer and Processing System
This repository is part of my MCE314 Mechatronics Engineering Design class. The goal of this project is to develop a system that streams images from a drone and sends them to a remote laptop for image processing.

Project Overview
This project involves two main scrpits:

Camera:
This script is responsible for sending image data from the drone to the laptop.
The image transfer is performed using a MJPEG Streaming Server, which sends unprocessed images over a local network from an RPi (Raspberry Pi) mounted on the drone to the laptop.

Camera Client:
This script processes the images received on the laptop using OpenCV's color detection library to detect and highlight specific colors based on user-defined ranges. The processed images are then displayed in a Tkinter window, showing the areas where the specified color is detected along with some statistical information about the detection.

# Camera Installation Guide

## Prerequisites

- **Python 3.x**: Ensure Python 3.x is installed on your system. Download it from the [official Python website](https://www.python.org/).
- **Webcam**: A webcam should be connected to your system for capturing video frames.
- **Network Configuration**: Ensure that port `8000` is open and not used by any other application.

## Step-by-Step Installation

### Step 1: Install Python

1. Download and install Python 3.x from the [official Python website](https://www.python.org/).
2. Verify the installation by opening a terminal or command prompt and typing:
   ```sh
   python --version

### Step 2: Set Up Virtual Enviroment

1. Open a terminal or command prompt.
2. Create a virtual environment by running:
    ```sh
    python -m venv myenv
3. Activate virtual enviroment
- On Windows:
    ```sh
   myenv\Scripts\activate
- On Mac/Linux:
   ```sh
   source myenv/bin/activate

### Step 3: Install OpenCV

1. With the virtual enviroment activated, install OpenCV using pip:
   ```sh
   pip install opencv-python

### Step 4: Save the Provided Code

1. Save the provided code in a file named 'camera3.py'

### Step 5: Run the Code

1. Execute the script in the terminal or command prompt
   ```sh
   python camera3.py

### Step 6: Access the Stream

1. Open a web browser and navigate to http://localhost:8000 to view the streaming video.



# Camera Client Installation

## Prerequisites

- **Python 3.x**: Ensure Python 3.x is installed on your system. Download it from the [official Python website](https://www.python.org/).
- **OpenCV**: Install using pip:
  ```sh
  pip install opencv-python
- **Pillow**: Install using pip:
  ```sh
  pip install pillow
- **Numpy**: Install using pip:
  ```sh
  pip install numpy

## Step-by-Step Installation
  
### Step 1: Install Python

1. Download and install Python 3.x from the [official Python website](https://www.python.org/).
2. Verify the installation by opening a terminal or command prompt and typing:
   ```sh
   python --version

### Step 2: Set Up Virtual Enviroment

1. Open a terminal or command prompt.
2. Create a virtual environment by running:
    ```sh
    python -m venv myenv
3. Activate virtual enviroment
- On Windows:
    ```sh
   myenv\Scripts\activate
- On Mac/Linux:
   ```sh
   source myenv/bin/activate

### Step 3: Install Required Libraries

1. With the virtual enviroment activated, install OpenCV using pip:
   ```sh
   pip install opencv-python pillow numpy

### Step 4: Save the Provided Code

1. Save the provided code in a file named 'camera client4.py'

### Step 5: Run the Code

1. Execute the script in the terminal or command prompt
   ```sh
   python camera client4.py

# Additional Configuration

Permissions
- Ensure you have the necessary permissions to access the webcam and open network ports.

Firewall Settings
- Configure your firewall to allow traffic on port 8000.

Troubleshooting
-Python Version: Ensure you are using Python 3.x.
-Dependencies: Verify that OpenCV is installed correctly in the virtual environment.
-Port Availability: Ensure port 8000 is not occupied by another application.

By following this guide, you should be able to successfully install and run the MJPEG Streaming Server using the provided Python code.
