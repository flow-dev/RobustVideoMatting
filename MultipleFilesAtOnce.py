import glob
import os
import subprocess

"""
Handle multiple files at once.

Example:
CUDA_VISIBLE_DEVICES=0 python3 MultipleFilesAtOnce.py
"""

def GenerateOutputPath(INPUT_PTH):
    # Generate Output Path
    dirname = os.path.dirname(INPUT_PTH)
    basename_without_ext = os.path.splitext(os.path.basename(INPUT_PTH))[0]
    #print(dirname, basename_without_ext)
    output_path = os.path.join(dirname,basename_without_ext)

    return output_path


def RunCommand(INPUT_PTH):

    # Generate output path
    output_path = GenerateOutputPath(INPUT_PTH)

    com_path = output_path + "_com.mp4"
    pha_path = output_path + "_pha.mp4"
    fgr_path = output_path + "_fgr.mp4"

    # RunCommand
    result = subprocess.call(["python3", "inference.py",
                            "--variant", "resnet50",
                            "--checkpoint", "rvm_resnet50.pth",
#                            "--variant", "mobilenetv3",
#                            "--checkpoint", "epoch-17-iter-330000.pth",
                            "--precision", "float16",
                            "--input-source", INPUT_PTH,
                            "--output-type", "video",
                            "--output-composition", com_path,
                            "--output-alpha", pha_path,
                            "--output-foreground", fgr_path])
    return result

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
    
    TARGET_DIR = "/data2/220910_Sancyoku_Remoteextras_edgecraft"

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
        result = RunCommand(video_file)
