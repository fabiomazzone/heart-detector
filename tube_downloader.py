from tqdm import tqdm
from pytube import YouTube
import os
from os.path import isfile, join
import cv2
from cv2 import VideoCapture

videos = ['https://youtu.be/HorTS-WNNBk', 'https://youtu.be/Mdx388nfzCY',
          'https://youtu.be/51aaWhfnzNQ', 'https://youtu.be/SS4ntXD10r8',
          'https://youtu.be/USjc1RwdiPY'
          ]


def download_videos(video_urls, path='videos'):
    for video in tqdm(video_urls):
        yt = YouTube(video)
        yt.\
            streams.\
            filter(progressive=True, file_extension='mp4').\
            first().\
            download(output_path=path)


def extract_frames(source_path='videos',
                   dest_path='frames',
                   filename_pattern='{dest}_{framestamp:.3f}.jpg'):
    source_files = [file for file in os.listdir(
        source_path) if isfile(join(source_path, file))]

    os.makedirs(dest_path)

    for file in source_files:
        video = VideoCapture(join(source_path, file))
        file_destination = join(dest_path, file)
        ret, frame = video.read()
        while(video.isOpened() and ret):
            timestamp = video.get(cv2.CAP_PROP_POS_MSEC)
            filename = filename_pattern.format(
                dest=file_destination,
                framestamp=round(timestamp, 3))

            cv2.imwrite(filename, frame)
            ret, frame = video.read()

        video.release()


if __name__ == "__main__":
    # download_videos(videos)
    extract_frames()
