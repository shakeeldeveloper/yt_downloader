from pytube import YouTube

def download_video(url, save_path="./"):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        video_stream.download(output_path=save_path)
        print("Download completed!")
    except Exception as e:
        print(f"Error: {e}")
