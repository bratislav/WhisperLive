from whisper_live.client import TranscriptionClient
commands = ["START_RECORDING", "STOP_RECORDING", "READ_OUT_LOUD", "DELETE_LAST_SENTENCE", "PRINT", "SHOW_DIAGNOSE_743"]
def detect_command(text):
  command = "NO_COMMAND"
  if "počni snimanje" in text or "snimaj" in text:
    command = "START_RECORDING"
  if "zaustavi snimanje" in text or "stopiraj snimanje" in text or "prestani snimanje" in text or "prestani da snimaš" in text:
    command = "STOP_RECORDING"
  return command
def process_command(command):
  print(f"Processing {command}")
def my_callback(text, segments):
  #print(text)
  command = detect_command(text.lower())
  if command != "NO_COMMAND":
    print(f"Detected command: {command}")
    process_command(command)
  else:
    print(text)    
client = TranscriptionClient(
  #"postdiphtheritic-alita-hurryingly.ngrok-free.dev",
  "localhost",
  #443,
  9090,
  #use_wss=True,
  lang="sr",
  translate=False,
  #model="large-v3-turbo",                                      # also support hf_model => `Systran/faster-whisper-small`
  model="small",
  use_vad=False,
  save_output_recording=False,                         # Only used for microphone input, False by Default
  output_recording_filename="./output_recording.wav", # Only used for microphone input
  mute_audio_playback=False,                          # Only used for file input, False by Default
  enable_translation=False
  #transcription_callback=my_callback,
  #log_transcription=False
)
client()
