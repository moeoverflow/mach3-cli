import ass
import os
import glob
import re
from mach3.encoding_convert import convertFile
from mach3.encoding_convert import convertedFiles

def timedelta_to_ass(td):
    r = int(td.total_seconds())

    r, secs = divmod(r, 60)
    hours, mins = divmod(r, 60)

    return "{hours:.0f}:{mins:02.0f}:{secs:02.0f}.{csecs:02}".format(
        hours=hours,
        mins=mins,
        secs=secs,
        csecs=td.microseconds // 10000
    )


def regex_process(text):
    return re.subn(r"{([^}]+?)}|(\\.)|(　)|()+", "", text)[0]


def get_dialogues(file_name):
    with open(file_name, "r") as rawFile:
        doc = ass.parse(rawFile)
        dialogues = []
        for event in doc.events:
            dialogues.append({"text": regex_process(event.text), "start": timedelta_to_ass(event.start), "end": timedelta_to_ass(event.end), "file": os.path.abspath(file_name)[:-4]})
        return dialogues


def recursive_index(dir):
    os.chdir(dir)
    all_dialogues = []
    for file in glob.glob('**/*.ass', recursive=True):
        all_dialogues.append(get_dialogues(convertFile(file)))
    for convertedFile in convertedFiles:
        os.remove(convertedFile)
    return all_dialogues
