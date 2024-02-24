from pyaudio import paInt32, PyAudio
from numpy import concatenate, frombuffer, int32, array
from scipy.io.wavfile import write
from keyboard import is_pressed

def record_sound(channels = 1, freq = 44100, chunk_size = 1024):
	global running
	format = paInt32  
	  
	p = PyAudio()

	stream = p.open(format=format, channels=channels, rate=freq, input=True, frames_per_buffer=chunk_size)

	frames = []
	print("Started Recording!!")
	print("Press q to stop recording")

	while running:
		data = stream.read(chunk_size)
		audio_array = frombuffer(data, dtype=int32)
		frames.append(audio_array)

		if is_pressed('q'):
			running = False

	print("Recording Stopped")
	stream.stop_stream()
	stream.close()
	p.terminate()

	audio_data = concatenate(frames)

	write("recording.wav", freq, audio_data)


running = False
print("Press S to start recording")
while not running:
	if is_pressed('s'):
		running = True
		record_sound()