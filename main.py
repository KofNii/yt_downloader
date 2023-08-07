from pytube import YouTube
import handlers as h

title =    ('''
 __     __         _______      _             _____                          _                    _             
 \ \   / /        |__   __|    | |           |  __ \                        | |                  | |            
  \ \_/ /___   _   _ | | _   _ | |__    ___  | |  | |  ___ __      __ _ __  | |  ___    __ _   __| |  ___  _ __ 
   \   // _ \ | | | || || | | || '_ \  / _ \ | |  | | / _ \\ \ /\ / /| '_ \ | | / _ \  / _` | / _` | / _ \| '__|
    | || (_) || |_| || || |_| || |_) ||  __/ | |__| || (_) |\ V  V / | | | || || (_) || (_| || (_| ||  __/| |   
    |_| \___/  \__,_||_| \__,_||_.__/  \___| |_____/  \___/  \_/\_/  |_| |_||_| \___/  \__,_| \__,_| \___||_|                                                                                                 

            ''')

def main():
    print(title)
    print('Welcome to YouTube Downloader, to get started, paste the URL of the video\n')
    url = input('> ')
    yt = YouTube(url)
    print(f"You choose: {yt.title}")
    opt = h.choice_handler('Choose an option:\n[1] Download the video\n[2] Download only the audio\n> ', 1, 2)
    if opt == 1: h.video_download(yt)
    else: h.audio_download(yt)
    input('Press [ENTER] to go back to main menu')
    main()

if __name__ == '__main__':
    main()

