from pytube import YouTube, Playlist

def download_youtube_video_with_audio(url, output_path='.'):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

        video_title = yt.title
        video_stream.download(output_path)

        print(f"Download of '{video_title}' with audio completed successfully.")
    except Exception as e:
        print("An error occurred during the download:", str(e))

def download_youtube_playlist_with_audio(playlist_url, output_path='.'):
    try:
        playlist = Playlist(playlist_url)
        playlist._video_regex = r"\"url\":\"(/watch\?v=[\w-]*)"

        playlist_title = playlist.title

        print(f"Downloading videos with audio from playlist: '{playlist_title}'")

        for video_url in playlist.video_urls:
            download_youtube_video_with_audio("https://www.youtube.com" + video_url, output_path)

        print(f"Download of all videos with audio from playlist: '{playlist_title}' completed.")
    except Exception as e:
        print("An error occurred during the download:", str(e))

if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/playlist?list=PLIhvC56v63IJVXv0GJcl9vO5Z6znCVb1P"
    download_youtube_playlist_with_audio(playlist_url, output_path='D:\Yt Playlists')
