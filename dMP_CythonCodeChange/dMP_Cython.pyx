import os
import cv2
import numpy as np
cimport numpy as np

cpdef extract_frames(str storage):
	cdef str video_file = "test.mp4"
	cdef float sensitivity = 0.05
	os.system('ffmpeg -i {} -vf  "select=gt(scene\\,{}), scale=300:300, showinfo" -vsync vfr {}%01d.jpg 2>&1 | findstr /r "pts_time:[0-9]*.[0-9]*" > timestamp.log '.format(video_file,sensitivity,storage))

cpdef tuple prepare_data(str storage):
	cdef list list1 = []
	cdef list frames = []
	frames = os.listdir(storage)
	cdef str fms
	cdef int f
	for fms in frames:
		f = int(fms.split(".")[0])
		list1.append(f)
	list1.sort(key=int)
	timestamps = prepare_timestamp(list1)
	frameData = prepare_frameData(storage,list1)
	return(timestamps,frameData)

cdef list prepare_timestamp(list list1):
	cdef list TsData = [] 
	cdef list timestamps = [] 
	cdef list withoutNewLine = []
	cdef str data, line, t

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

cdef list prepare_frameData(str storage, list list1):
	cdef test_data = []
	cdef np.ndarray im
	cdef int frame
	for frame in list1:
		im = cv2.imread(storage+str(frame)+".jpg")
	return test_data
