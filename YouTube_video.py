from pytube import Playlist

playlist = input (" paste your list")
print('Number of videos in playlist: %s' % len(playlist.video_urls))
playlist.download_all()