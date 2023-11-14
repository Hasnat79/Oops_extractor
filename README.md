# Oops Video Dataset Processing

## Overview

This project focuses on processing the [Oops Video Dataset](https://oops.cs.columbia.edu/data/) for identifying and extracting videos with unusual events based on the provided transition times. The dataset includes validation videos, and the goal is to extract videos labeled as having unusual events.

## Code Structure

The project code is organized into a Python script named extract_failed_videos.py. The script performs the following steps:

1. Importing Libraries:

   - json: Used for reading JSON files.
   - os: Provides a way of interacting with the operating system.
   - shutil: Used for file operations like copying files.
   - tqdm: A library for creating progress bars.

2. File Paths:

   - tt_path: Path to the transition time file (./oops_dataset/annotations/transition_times_fixed.json).
   - val_dir_path: Path to the directory containing validation set videos (./oops_dataset/oops_video/val/).
  -  oops_all_failed_videos_val_dir_new: Path to the directory where failed videos will be extracted (./oops_all_failed_videos_val_dir_new/).

3. Loading Transition Times:

   - Reads the transition times from the specified JSON file into the transition_time dictionary.

4. Video Extraction:

   - Iterates through each key-value pair in transition_time.
 -   Checks if the corresponding video file exists in the validation set directory.
   - If the video exists and has no failures labeled (i.e., n_notfound is 0), it is copied to the destination directory.

5. Summary:

  -  Prints a message indicating the completion of the file extraction process.
  -  Calculates and prints the total number of files extracted.

## Usage

To use this script, make sure you have the Oops Video Dataset in the specified directory structure. Run the script in a Python environment, and it will extract videos with unusual events to the designated directory.

```bash

python extract_failed_videos.py
```



## Notes

  -  Ensure that the required libraries (json, os, shutil, tqdm) are installed in your Python environment.
   - The file paths may need to be adjusted based on the actual directory structure of the Oops Video Dataset.

## Contact
Feel free to reach out if you have any questions or suggestions!
- 📧 Email: hasnatabdullah79@gmail.com
- 💼 LinkedIn: [Hasnat Md Abdullah ](https://www.linkedin.com/in/hasnat-md-abdullah/)
