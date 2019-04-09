import os
import cv2
import numpy as np

def extract_frames(storage):
	video_file = "test.mp4"
	sensitivity = 0.05
	os.system('ffmpeg -i {} -vf  "select=gt(scene\\,{}), scale=300:300, showinfo" -vsync vfr {}%01d.jpg 2>&1 | findstr /r "pts_time:[0-9]*.[0-9]*" > timestamp.log '.format(video_file,sensitivity,storage))

def prepare_data(storage):
	list1 = []
	frames = os.listdir(storage)
	for fms in frames:
		fms = int(fms.split(".")[0])
		list1.append(fms)
	list1.sort(key=int)
	timestamps = prepare_timestamp(list1)
	frameData = prepare_frameData(storage,list1)
	return(timestamps,frameData)

def prepare_timestamp(list1):
	TsData = []
	timestamps = []
	with open("timestamp.log") as f:
		data = f.read()
	withoutNewLine = data.split("\n")
	for line in withoutNewLine:
		if "pts_time:" in line:
			TsData.append(line.split("pts_time:")[1])
	for data in TsData:
		t = data.split(" ")[0]
		timestamps.append(t)
	return timestamps

def prepare_frameData(storage,list1):
	test_data = []
	for frame in list1:
		im = cv2.imread(storage+str(frame)+".jpg")
		test_data.append(im)

	test_data = np.array(test_data)
	return test_data
