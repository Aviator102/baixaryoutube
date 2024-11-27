from pytubefix import YouTube

def download_video_1080p(url):
    RES = '1080p'
    yt = YouTube(url)

    for idx, i in enumerate(yt.streams):
        if i.resolution == RES:
            break
    video = yt.streams[idx].download('video', 'video.mp4')
    print(f"✅ Vídeo baixado em: {video}")

def download_audio(url):
    yt = YouTube(url)
    ys = yt.streams.get_audio_only()
    audio = ys.download('video', 'audio.mp4')
    print(f"✅ Áudio baixado em: {audio}")

if __name__ == "__main__":
    url = input("Cole aqui o link do vídeo do YouTube que deseja baixar: ").strip()
    
    try:
        download_video_1080p(url)
        download_audio(url)
    except Exception as e:
        print(f"❗Erro ao baixar o vídeo ou áudio: {e}")
