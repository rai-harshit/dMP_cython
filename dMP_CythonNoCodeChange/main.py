from dMP_Cython import extract_frames, prepare_data
storage = ".\\storage\\frames\\"
extract_frames(storage)
data = prepare_data(storage)
print("Done")