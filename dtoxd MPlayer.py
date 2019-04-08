# Importing Libraries : Start
from keras.models import load_model
import os
import cv2
import numpy as np
import time
import shutil
from subprocess import Popen, PIPE
# Imporing Libraries : End

# Defining Constant & Loading Model : Start
video_file = "GET FILE NAME HERE WITH COMPLETE PATH"
unique_file_identifier = "SOME UNIQUE IDENTIFIER FROM PASSED FILE"
storage = ".\\storage\\"

# model_file = storage+"\\model.h5"
frames_store = storage+"\\frames\\+{}".format(unique_file_identifier)
sensitivity = 0.05
# model = load_model(model_file)
# Defining Constant & Loading Model : End

# Frame Extraction : Start

# os.system('ffmpeg -i {} -vf  "select=gt(scene\\,{}), scale=300:300, showinfo" -vsync vfr {}%01d.jpg 2>&1 | findstr /r "pts_time:[0-9]*.[0-9]*" > timestamp_{}.log '.format(video_file,sensitivity,frames_store,unique_file_identifier))
Popen('ffmpeg -i {} -vf  "select=gt(scene\\,{}), scale=300:300, showinfo" -vsync vfr {}%01d.jpg 2>&1 | findstr /r "pts_time:[0-9]*.[0-9]*" > timestamp_{}.log '.format(video_file,sensitivity,frames_store,unique_file_identifier))
# Frame Extraction : End

# Frame Processing : Start
# list1 = []
# TsData = []
# timestamps = []
# test_data = []
# result = []
# explicit_durations = []

# frames = os.listdir(frames_store)
# for fms in frames:
# 	fms = int(fms.split(".")[0])
# 	list1.append(fms)
# list1.sort(key=int)

# with open("timestamp_{}.log".format(unique_file_identifier)) as f:
#     data = f.read()

# withoutNewLine = data.split("\n")
# for line in withoutNewLine:
#     if "pts_time:" in line:
#         TsData.append(line.split("pts_time:")[1])

# for data in TsData:
#     t = data.split(" ")[0]
#     timestamps.append(t)

# for frame in list1:
# 	im = cv2.imread(frames_store+str(frame)+".jpg")
# 	test_data.append(im)

# test_data = np.array(test_data)

# # Test Data Prediction : Start
# predictions = model.predict(test_data)
# # Test Data Prediction : End

# # Post-prediction Processing : Start
# for prediction in predictions:
# 	if prediction[0]>prediction[1]:
# 		result.append(1)
# 	else:
# 		result.append(0)

# for data in zip(list1,timestamps,result):
# 	if data[2] == 1:
# 		explicit_durations.append(data[1])
# # Post-prediction Processing : End

# # Moderating Explicit Content : Start
# if len(explicit_durations) > 0:
# 	conditions = []
# 	last_explicit_duration = 0
# 	for duration in explicit_durations:
# 		if float(duration)-last_explicit_duration<1:
# 			conditions.append("between(t,{},{})".format(float(last_explicit_duration),float(duration)+0.1))
# 		else:
# 			conditions.append("between(t,{},{})".format(float(duration),float(duration)+0.1))
# 		last_explicit_duration = float(duration)
# 	final_condition = "+".join(conditions)
# 	os.system("ffmpeg -i {} -q:v 1 -qmin 1 -filter_complex \"boxblur=270.0:enable='if({},1,0)\" -codec:a copy test.avi | vlc test.avi".format(video,final_condition))
# else:
# 	os.system("vlc {}".format(video_file))
# # Moderating Explicit Content : End

# # Post-process CleanUp