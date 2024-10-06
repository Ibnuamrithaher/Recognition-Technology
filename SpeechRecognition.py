from moviepy.editor import VideoFileClip
import speech_recognition as sr

# Path ke video MP4
video_path = 'C:/Users/TUF GAMING/Downloads/vid8.mp4'
# Path untuk menyimpan file audio dalam format WAV
audio_output_path = 'C:/Users/TUF GAMING/Downloads/output_audio.wav'

# Langkah 1: Ekstraksi Audio dari Video
try:
    # Load video file
    video = VideoFileClip(video_path)

    # Ekstrak audio dari video
    audio = video.audio

    # Simpan audio dalam format WAV
    audio.write_audiofile(audio_output_path)
    print(f"Audio berhasil diekstrak ke {audio_output_path}")

    # Tutup sumber daya
    audio.close()
    video.close()

except Exception as e:
    print(f"Terjadi kesalahan saat ekstraksi audio: {e}")

# Langkah 2: Transkripsi Audio Menggunakan SpeechRecognition
try:
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load the extracted audio file
    with sr.AudioFile(audio_output_path) as source:
        audio_data = recognizer.record(source)
        # Transcribe audio to text
        transcript = recognizer.recognize_google(audio_data, language='id-ID')
        print("Transkripsi berhasil:")
        print(transcript)

except sr.UnknownValueError:
    print("Audio tidak dapat dikenali.")
except sr.RequestError:
    print(sr.RequestError)
    print("Tidak dapat meminta hasil. Periksa koneksi.")
except Exception as e:
    print(f"Terjadi kesalahan saat transkripsi: {e}")
