from whisper_live.client import TranscriptionClient
def my_callback(text, segments):
  print(text)
client = TranscriptionClient(
  "postdiphtheritic-alita-hurryingly.ngrok-free.dev",
  443,
  use_wss=True,
  lang="sr",
  translate=False,
  model="large-v3-turbo",                                      # also support hf_model => `Systran/faster-whisper-small`
  use_vad=False,
  save_output_recording=False,                         # Only used for microphone input, False by Default
  output_recording_filename="./output_recording.wav", # Only used for microphone input
  mute_audio_playback=False,                          # Only used for file input, False by Default
  enable_translation=False,
  transcription_callback=my_callback
)
client()
