import os
def main():
    global cover
    global song
    global out
    cover = input("song file path ")
    song = input("cover image file path ")
    out = input("output filename ")
    qual = input("quality (bitrate) ")
    # replace " X:/music_script/flv/" with the *full* file path of the "flv" folder
    os.system("ffmpeg -i " + cover + " -i " + song + " -vf format=yuv420p" " X:/music_script/flv/" + out + ".flv")    
    # replace "X:\HandBrakeCLI-1.5.1-win-x86_64\HandBrakeCLI.exe " with the *full* file path to the HandBrake CLI executable
    # again, replace " X:/music_script/flv/" with the *full* file path of the "flv" folder
    os.system("X:\HandBrakeCLI-1.5.1-win-x86_64\HandBrakeCLI.exe " + "-i " + "X:/music_script/flv/" + out + ".flv" + " -o " + "X:/music_script/" + out + ".webm" + " -q 55 " + "-B " + qual + " -f av_webm" + " -e VP8" + " -X 480" + " -Y 480")
    # replace " X:/music_script/mp4/" with the *full* file path of the "mp4" folder
    os.system("cp " + "X:/music_script/" + out + ".webm " + "X:/music_script/mp4/" + out + ".mp4")
    os.system("cls")
    main()
main()
