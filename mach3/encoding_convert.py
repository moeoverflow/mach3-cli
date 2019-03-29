import codecs
import os
from chardet import detect

convertedFiles = []

def get_encoding_type(fileName):
    with open(fileName, "rb") as f:
        rawdata = f.read()
    return detect(rawdata)["encoding"]



def convertFile(srcfile):
    print(srcfile, get_encoding_type(srcfile))
    trgfile = srcfile + "utf8"
    # if get_encoding_type(srcfile) == "utf-8":
    #     pass
    # else:
    try:
        with open(srcfile, "r", encoding=get_encoding_type(srcfile)) as f, open(trgfile, "w",
                                                                                encoding="utf-8") as e:
            text = f.read()
            e.write(text)

        convertedFiles.append(trgfile)
        return trgfile
    except UnicodeDecodeError:
        print("Decode Error")
    except UnicodeEncodeError:
        print("Encode Error")