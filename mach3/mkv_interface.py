import os
from shlex import quote


def mkv_play(fileName, start, end):
    sub_name = fileName
    vid_name = sub_name[:-4] + ".mkv"

    command = "mpv --window-scale=0.5 --pause --keep-open=yes --start={} --end={} --sub-file={} {}"\
        .format(quote(start), quote(end), quote(sub_name), quote(vid_name))

    os.system(command)