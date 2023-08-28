
# Script to split a video into multiple images.
# Usage: python splitter.py input_video_path frames_to_jump output_image_folder

import cv2
import os
import argparse



def split_video_into_images(video_path, frames_to_jump, output_folder):
    # Get the video name without extension
    video_name_split = os.path.splitext(os.path.basename(video_path))
    video_name = video_name_split[0] + "_image_split"
    output_folder = os.path.join(output_folder, video_name)
    os.makedirs(output_folder, exist_ok=True)

    # Open the video for reading
    cap = cv2.VideoCapture(video_path)

    # Variable to count frames
    frame_count = 0

    # Number of frames to skip before capturing an image
    frames_to_skip = frames_to_jump

    # Loop to read frames from the video
    while cap.isOpened():
        # Read the current frame
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            break

        # Increment frame count
        frame_count += 1

        # If the frame count is divisible by the frames to skip,
        # save the frame as a JPG image
        if frame_count % frames_to_skip == 0:
            image_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(image_path, frame)
            print(f"Saving frame {frame_count}")

    # Close the video and release resources
    cap.release()

if __name__ == "__main__":
    # Configure command-line argument parsing
    parser = argparse.ArgumentParser(description="Split a video into images.")
    parser.add_argument("video_path", type=str, help="Path to the input video")
    parser.add_argument("frames_to_jump", type=int, help="Every how many frames you would like to jump")
    parser.add_argument("output_folder", type=str, help="Path to the output folder for images")
    args = parser.parse_args()

    # Call the function to split the video into images
    split_video_into_images(args.video_path, args.frames_to_jump, args.output_folder)
