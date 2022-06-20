from tqdm import tqdm
from pytube import YouTube

videos = ['https://youtu.be/HorTS-WNNBk', 'https://youtu.be/Mdx388nfzCY',
          'https://youtu.be/51aaWhfnzNQ', 'https://youtu.be/SS4ntXD10r8']


def download_videos(video_urls, path='videos'):
    for video in tqdm(video_urls):
        yt = YouTube(video)
        yt.\
            streams.\
            filter(progressive=True, file_extension='mp4').\
            first().\
            download(output_path=path)


if __name__ == "__main__":
    download_videos(videos)
