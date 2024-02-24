from PIL import ImageGrab
import cv2 as cv
from numpy import concatenate, frombuffer, int32, array
from pyaudio import paInt32, PyAudio
from scipy.io.wavfile import write
from moviepy.editor import VideoFileClip, AudioFileClip, clips_array
from os import remove
from threading import Thread
from keyboard import is_pressed
from time import time
import tkinter as tk


def rescale(frame, scale = 0.3):
	height = int(frame.shape[0] * scale)
	width = int(frame.shape[1] * scale)
	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


def record(fps = 60.0):
	vid_codec = cv.VideoWriter_fourcc('M','J','P','G')
	img = ImageGrab.grab()
	img_arr = array(img)
	shape = img_arr.shape
	out = cv.VideoWriter("Video.avi", vid_codec , fps, (shape[1], shape[0]))
	start_time = time()

	while True:
		current_time = time()
		elapsed_time = current_time - start_time
		if elapsed_time >= 1/fps:
			image = ImageGrab.grab()
			img_np_arr = array(image)
			final_img = cv.cvtColor(img_np_arr, cv.COLOR_RGB2BGR)
			out.write(final_img)
			start_time = current_time

		if is_pressed('q'):
			break

	out.release()
	cv.destroyAllWindows()


def record_sound(channels = 1, freq = 44100, chunk_size = 1024):
	format = paInt32  
	  
	p = PyAudio()
	stream = p.open(format=format, channels=channels, rate=freq, input=True, frames_per_buffer=chunk_size)

	frames = []

	while True:
		data = stream.read(chunk_size)
		audio_array = frombuffer(data, dtype=int32)
		frames.append(audio_array)

		if is_pressed('q'):
			break

	stream.stop_stream()
	stream.close()
	p.terminate()

	audio_data = concatenate(frames)
	write("recording.wav", freq, audio_data)


def live_view():
	capture = cv.VideoCapture(0)

	while True:
		isTrue, own_frame = capture.read()
		own_frame = rescale(own_frame)
		cv.imshow('Recording', own_frame)

		cv.waitKey(1)
		if is_pressed('q'):
			break

	cv.destroyAllWindows()


def edit(scr_title = "Screen_Recording"):
	root.withdraw()

	view_thread = Thread(target = live_view)
	view_thread.start()

	record_thread = Thread(target = record)
	record_thread.start()

	sound_thread = Thread(target = record_sound)
	sound_thread.start()

	view_thread.join()
	record_thread.join()
	sound_thread.join()

	if names.get() != "":
		scr_title = str(names.get())
	else:
		pass

	names.delete(0, tk.END)

	while True:
		if is_pressed('q'):
			root.deiconify()
			break

	video_clip = VideoFileClip("Video.avi")
	audio_clip = AudioFileClip("recording.wav")
	video_clip = video_clip.set_audio(audio_clip)
	video_clip.write_videofile(f"{scr_title}.avi", codec="libx264", audio_codec="aac")
	video_clip.close()
	audio_clip.close()
		
	try:
		remove("Video.avi")
		remove("recording.wav")

	except:
		pass


# GUI
root = tk.Tk()
root.geometry("600x200")
root.title("Screen Recorder")


title = tk.Label(root, text = "Screen Recorder", font = ("Arial", 50), padx = 50, pady = 10)
guide = tk.Label(root, text = "Press q to end recording", font = ("Arial", 20), pady = 5)
names = tk.Entry(root, font = ("Arial", 20), width = 30)
button = tk.Button(root, text = "Start Recording", font = ("Arial", 20), command = edit)


title.grid(row = 0, column = 0, columnspan = 2)
guide.grid(row = 1, column = 0, columnspan = 2)
names.grid(row = 2, column = 0, pady = 5, sticky = "w")
button.grid(row = 2, column = 1, pady = 5, sticky = "e")

root.mainloop()