# Video to Images Splitter for Computer Vision

This script enables the easy extraction of frames from a video, making it a valuable tool for generating datasets for computer vision tasks. Instead of manually capturing images, you can record a video containing various elements of interest for your computer vision annotation. This script will then split the video into individual images that can be utilized for annotation purposes.

## Usage

1. **Clone the Repository:** Start by cloning this repository to your local machine:

   ```bash
   git clone https://github.com/johnhdeleon/CVToolKit.git

2. **Navigate to the Directory:** Move into the project directory:
   ```bash
    cd video-to-images-splitter

3. **Install Dependencies:** If you haven't already, install the required dependencies by creating a virtual environment and running:
   ```bash
   pip install -r requirements.txt
4. **Run the script:** Execute the script by providing the path to the input video, the number of frames to skip, and the output folder for images:
   ```bash
   python splitter.py input_video.mp4 frames_to_skip output_image_folder/
- `input_video.mp4`: Path to the input video file.
- `frames_to_skip`: Number of frames to skip before capturing an image.
- `output_image_folder/`: Path to the output folder where images will be saved.
5. **Example Use Case**:
Consider a scenario where you're training an object detection model and need a dataset with annotated objects in various poses and backgrounds. Instead of manually capturing images for each pose, record a video in which the objects appear in different configurations. Then, use this script to split the video into individual images. These images will retain the context and temporal information, improving the richness of your dataset.
Feel free to customize the script and use it to optimize your data collection process for computer vision projects!





