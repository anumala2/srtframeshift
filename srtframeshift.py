"""
title           :srtframeshift.py
description     :A program made to "frameshift" an .srt file's subtitles by a given number of seconds.
author          :Aadithya Anumala
date            :02/05/2020
version         :0.5
usage           :python3 srtframeshift.py
notes           :
python_version  :3.7.6 
"""

import datetime
infilename = input("File you'd like to frameshift (leave out the .srt):\n")
outfilename = input("File you'd like to output to (leave out the .srt):\n")
shiff = ""
while(type(shiff) != int):
    try:
        shiff = input("How many seconds do you want to frameshift? (For it to go back use \'-\'): \n")
        shiff = int(shiff)
    except:
        print("Enter an integer.")
file = open(infilename + ".srt", "r")
wrif = open(outfilename + ".srt",'w')

def splitit(times):
    times[0] = times[0].replace(",", ":")
    times[2] = times[2].replace(",", ":")
    first = times[0].split(":")
    second = times[2].split(":")
    times[0].replace(",", "")
    times[2].replace(",", "")
    return first + second

def frameshift(arrish, shift):
    try:
        a = datetime.timedelta(0,int(arrish[2]),0,int(arrish[3]),int(arrish[1]),int(arrish[0]))
        b = a + datetime.timedelta(0,int(shift%59))
        for i in range(0,int(shift/59)):
            b = b + datetime.timedelta(0,59) # days, seconds, then other fields.
        c = datetime.timedelta(0,int(arrish[6]),0,int(arrish[7]),int(arrish[5]),int(arrish[4]))
        d = c + datetime.timedelta(0,int(shift%59))
        for i in range(0,int(shift/59)):
            d = d + datetime.timedelta(0,59) # days, seconds, then other fields.
        b = datetime.datetime(1,1,1)+b
        d = datetime.datetime(1,1,1)+d
    except:
        print(arrish)
    
    return "{:02d}:{:02d}:{:02d},{:03d} --> {:02d}:{:02d}:{:02d},{:03d}".format(b.hour, b.minute, b.second,
                                                int(b.microsecond/1000), d.hour, d.minute, d.second, int(d.microsecond/1000))

for line in file:
    if line[0] == "0":
        times = line.split(" ")
        wrif.write(frameshift(splitit(times), shiff) + "\n")
    else:
        wrif.write(line)
