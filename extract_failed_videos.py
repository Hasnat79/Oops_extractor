import json
import os
import shutil
from tqdm import tqdm
#transition_time file importing
tt_path = "./oops_dataset/annotations/transition_times_fixed.json"

# OOPS- validation set dir path 
val_dir_path = "./oops_dataset/oops_video/val/"
oops_all_failed_videos_val_dir_new = "./oops_all_failed_videos_val_dir_new/"

with open(tt_path, 'r') as f: 
    transition_time = json.load(f)

# print(transition_time)
for k,v in tqdm(transition_time.items()):


    if os.path.isfile(val_dir_path+k+".mp4"):
        
        source = val_dir_path+k+".mp4"
        dest = oops_all_failed_videos_val_dir_new+k+".mp4"

        # Number of workers who labeled failure not found (means: everybody labeled--> this video had unusual event)
        if v["n_notfound"]==0:
            shutil.copy(source, dest)
    
    
print("file extraction to oops_all_failed_videos_val done!")

total = sum(len(files) for _, _, files in os.walk(oops_all_failed_videos_val_dir_new))
print(f"total files extracted: {total}")

