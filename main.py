# FILE ORGANIZER
import os
import shutil

image_formats = ["jpg", "png", "jpeg", "gif", "webp", "tiff", "HEIC"]
audio_formats = ["mp3", "wav"]
video_formats = ["mp4", "avi", "webm", "mov"]
docs_formats = ["ai", "ait", "txt", "rtf"]

files = os.listdir("./")

for file in files:
    if os.path.isfile(file):
        ext = (file.split(".")[-1]).lower()

        if ext in image_formats:
            shutil.move(file, "images/"+file)
        elif ext in audio_formats:
            shutil.move(file, "audio/"+file)
        elif ext in video_formats:
            shutil.move(file, "videos/"+file)
        elif ext in docs_formats:
            shutil.move(file, "docs/"+file)
        else:
            shutil.move(file, "others/"+file)
