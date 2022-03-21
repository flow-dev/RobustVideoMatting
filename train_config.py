"""
Expected directory format:

VideoMatte Train/Valid:
    ├──fgr/
      ├── 0001/
        ├── 00000.jpg
        ├── 00001.jpg
    ├── pha/
      ├── 0001/
        ├── 00000.jpg
        ├── 00001.jpg
        
ImageMatte Train/Valid:
    ├── fgr/
      ├── sample1.jpg
      ├── sample2.jpg
    ├── pha/
      ├── sample1.jpg
      ├── sample2.jpg

Background Image Train/Valid
    ├── sample1.png
    ├── sample2.png

Background Video Train/Valid
    ├── 0000/
      ├── 0000.jpg/
      ├── 0001.jpg/

"""


DATA_PATHS = {
    
    'videomatte': {
        'train': '/data2/BackgroundMattingV2_Dataset/VideoMatte240K_JPEG_SD/train',
        'valid': '/data2/BackgroundMattingV2_Dataset/VideoMatte240K_JPEG_SD/test',
    },
    'imagematte': {
        'train': '/data2/RVM/ImageMatte/train_human',
        'valid': '/data2/Kaijin_Mask_Dataset/Kaijin_Valid/jpg',
    },
    'background_images': {
        'train': '/data2/BackgroundMattingV2_Dataset/Backgrounds/PASS_dataset_000/0',
        'valid': '/data2/BackgroundMattingV2_Dataset/Backgrounds/train',
    },
    'background_videos': {
        'train': '/data2/BackgroundMattingV2_Dataset/BackgroundVideosTrain/train',
        'valid': '/data2/BackgroundMattingV2_Dataset/BackgroundVideosTest/test',
    },
    
    
    'coco_panoptic': {
        'imgdir': '/data2/MSCOCO/train2017/',
        'anndir': '/data2/MSCOCO/panoptic_annotations_trainval2017/annotations/panoptic_train2017/',
        'annfile': '/data2/MSCOCO/panoptic_annotations_trainval2017/annotations/panoptic_train2017.json',
    },
    'spd': {
        'imgdir': '/data2/SuperviselyPersonDataset/img',
        'segdir': '/data2/SuperviselyPersonDataset/seg',
    },
    'youtubevis': {
        'videodir': '/data2/YouTubeVIS_2021/train/JPEGImages',
        'annfile': '/data2/YouTubeVIS_2021/train/instances.json',
    }
    
}
