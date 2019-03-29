import os
from shlex import quote


def mkv_play(fileName, start, end):
    sub_name = fileName
    vid_name = sub_name[:-4]

    if os.path.exists(vid_name + ".mkv"):
        command = "mpv --window-scale=0.5 --pause --keep-open=yes --start={} --sub-file={} {}"\
        .format(quote(start), quote(sub_name), quote(vid_name + ".mkv"))
    elif os.path.exists(vid_name + ".mp4"):
        command = "mpv --window-scale=0.5 --pause --keep-open=yes --start={} --sub-file={} {}"\
        .format(quote(start), quote(sub_name), quote(vid_name + ".mp4"))
    elif os.path.exists(vid_name + ".mov"):
        command = "mpv --window-scale=0.5 --pause --keep-open=yes --start={}--sub-file={} {}"\
        .format(quote(start), quote(sub_name), quote(vid_name + ".mov"))
    else:
        print("I cannot find the matching video file for you, Misaka tries and fails. \nPlease make sure they have the same file name.")
        exit(1)

    print(command)
    os.system(command)