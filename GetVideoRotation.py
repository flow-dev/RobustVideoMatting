import glob
import json
import os
import shlex
import subprocess
from moviepy.editor import *


"""
Get the rotation of the video and rewrite the meta
<https://stackoverflow.com/questions/41200027/how-can-i-find-video-rotation-and-rotate-the-clip-accordingly-using-moviepy>

Example:
python3 GetVideoRotation.py
"""

def GenerateOutputPath(INPUT_PTH):
    # Generate Output Path
    dirname = os.path.dirname(INPUT_PTH)
    basename_without_ext = os.path.splitext(os.path.basename(INPUT_PTH))[0]
    #print(dirname, basename_without_ext)
    output_path = os.path.join(dirname,basename_without_ext)
    return output_path


def get_rotation(file_path_with_file_name):
    """
    Function to get the rotation of the input video file.
    Adapted from gist.github.com/oldo/dc7ee7f28851922cca09/revisions using the ffprobe comamand by Lord Neckbeard from
    stackoverflow.com/questions/5287603/how-to-extract-orientation-information-from-videos?noredirect=1&lq=1

    Returns a rotation None, 90, 180 or 270
    """
    cmd = "ffprobe -loglevel error -select_streams v:0 -show_entries stream_tags=rotate -of default=nw=1:nk=1"
    args = shlex.split(cmd)
    args.append(file_path_with_file_name)
    # run the ffprobe process, decode stdout into utf-8 & convert to JSON
    ffprobe_output = subprocess.check_output(args).decode('utf-8')
    if len(ffprobe_output) > 0:  # Output of cmdis None if it should be 0
        ffprobe_output = json.loads(ffprobe_output)
        rotation = ffprobe_output

    else:
        rotation = 0

    return rotation

def OverWriteRotationMeta(INPUT_PTH):

    # Generate output path
    output_path = GenerateOutputPath(INPUT_PTH)

    rotate_path = output_path + "_rotate.mp4"

    rotation = get_rotation(INPUT_PTH)
    if rotation == 90:  # If video is in portrait
       # RunCommand
        result = subprocess.call(["ffmpeg", "-i", INPUT_PTH, "-metadata:s:v:0", "rotate=0",rotate_path])
#        result = subprocess.call(["rm", INPUT_PTH])
    elif rotation == 270:  # Moviepy can only cope with 90, -90, and 180 degree turns
        # RunCommand
        result = subprocess.call(["ffmpeg", "-i", INPUT_PTH, "-metadata:s:v:0", "rotate=0",rotate_path])
#        result = subprocess.call(["rm", INPUT_PTH])
    elif rotation == 180:
        # RunCommand
        result = subprocess.call(["ffmpeg", "-i", INPUT_PTH, "-metadata:s:v:0", "rotate=0",rotate_path])
#        result = subprocess.call(["rm", INPUT_PTH])
    return rotation


def PrintDataGroupList(TARGET_DIR):
    '''Show Print DataGroup List'''
    group_list = [*glob.glob(os.path.join(TARGET_DIR, '**'), recursive=True)]
    print(group_list)
    print("DataGroup-Num:",len(group_list))
    return

def PrintDataGroupExt(TARGET_DIR):
    '''Search for extensions'''
    group_list = [*glob.glob(os.path.join(TARGET_DIR, '**'), recursive=True)]
    ext_list = []
    for name in group_list:
        base, ext = os.path.splitext(name)
        if(ext):
            ext_list.append(ext)
    print(ext_list, len(ext_list))
    return

def GetDataGroupListWithExt(TARGET_DIR, ext):
    '''Get DataGroup with Ext'''
    group_list = sorted([*glob.glob(os.path.join(TARGET_DIR, '**', '*.' + ext), recursive=True)])
    print(group_list)
    print("DataGroup-Num:",len(group_list))
    return group_list


if __name__ == '__main__':
    
    TARGET_DIR = "../../Sanc_eki_video_220228"

    # DataGroup Debug
    PrintDataGroupList(TARGET_DIR)
    PrintDataGroupExt(TARGET_DIR)

    # GetDataGroupListWithExt
    mp4_list = GetDataGroupListWithExt(TARGET_DIR, "mp4")
    mov_list = GetDataGroupListWithExt(TARGET_DIR, "MOV")

    # Merge lists
    video_list = mp4_list + mov_list
    print(video_list, len(video_list))

    # Loop
    for idx, video_file in enumerate(video_list):
        print(idx, "/", len(video_list))
        print(video_file)
        rotation = OverWriteRotationMeta(video_file)
        print(rotation)