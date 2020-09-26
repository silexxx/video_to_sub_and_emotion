import os

command1="ffmpeg -i data/input.mp4 -vn -acodec pcm_s16le -ar 44100 -ac 2 -y output_audio/output.wav"	
os.system(command1)

command2 = "python final.py"
os.system(command2)

command3="ffmpeg -i output/output.avi -i output_audio/output.wav -c:v copy -map 0:v:0 -map 1:a:0 -c:a aac -b:a 192k -y output/input.avi"
os.system(command3)


command4="python3 autosub/main.py --file data/input.mp4"
os.system(command4)

command4="rm output/final.avi"
command5="rm output/output.avi"
command6="rm output_audio/output.wav"
command7="rm audio/*"

# os.system(command4)
os.system(command5)
os.system(command6)
os.system(command7)