from pytubefix import YouTube
 
def download_video_1080p(url):
    RES = '1080p'
    yt = YouTube(url)

    for idx,i in enumerate(yt.streams):
        if i.resolution == RES:
            break
    video = yt.streams[idx].download('video', 'video.mp4')
    print(video)

def download_audio(url):
    yt = YouTube(url)
    ys = yt.streams.get_audio_only()
    audio = ys.download('video', 'audio.mp4')
    print(audio)

url = "https://www.youtube.com/watch?v=11d6dtBUEXI"

download_video_1080p(url)
download_audio(url)