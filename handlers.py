from os import rename, path

def choice_handler(txt, mn, mx):
    while True:
        try:
            x = int(input(txt))
        except ValueError:
            print(f"{x} is not a valid choice!")
        if x < mn or x > mx:
            print(f"{x} is not a valid choice!")
        else: return x

def video_download(vid):
    print(f"Downloading {vid.title}...")
    vid.streams.get_highest_resolution().download()
    print('The video was downloaded successfully')

def audio_download(aud):
    print(f"Downloading {aud.title} audio...")
    out_file = aud.streams.get_audio_only().download()
    base, ext = path.splitext(out_file)
    new_file = base + '.mp3'
    rename(out_file, new_file)
    print('The audio was downloaded successfully')
