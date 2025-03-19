# Step1a: Setup Text to Speech–TTS–model with gTTS
import platform
import subprocess
from elevenlabs.client import ElevenLabs
import elevenlabs
import os
from gtts import gTTS
from dotenv import load_dotenv
from pydub import AudioSegment


def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = "en"

    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text = "Hi this is Ai with Hassan eleven labs!"
# text_to_speech_with_gtts_old(
#     input_text=input_text, output_filepath="gtts_testing.mp3")

# Step1b: Setup Text to Speech–TTS–model with ElevenLabs
load_dotenv()
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")


def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)


# text_to_speech_with_elevenlabs_old(
#     input_text, output_filepath="elevenlabs_testing.mp3")

# Step2: Use Model for Text output to Voice

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"

    # Generate the speech
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

    # Convert MP3 to WAV using pydub
    wav_filepath = output_filepath.replace('.mp3', '.wav')
    audio = AudioSegment.from_mp3(output_filepath)
    audio.export(wav_filepath, format="wav")

    os_name = platform.system()

    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', wav_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(
                ['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', wav_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


# Test
input_text = "Hi this is Ai with Hassan, autoplay testing!"
# text_to_speech_with_gtts(input_text=input_text,
#                          output_filepath="gtts_testing_autoplay.mp3")


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    # Generate audio from ElevenLabs API
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )

    # Save the audio file as MP3
    elevenlabs.save(audio, output_filepath)

    # Convert the MP3 file to WAV using pydub
    wav_filepath = output_filepath.replace('.mp3', '.wav')
    audio_segment = AudioSegment.from_mp3(output_filepath)
    audio_segment.export(wav_filepath, format="wav")

    os_name = platform.system()

    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', wav_filepath])
        elif os_name == "Windows":  # Windows
            # Use Media.SoundPlayer to play the WAV file
            subprocess.run(
                ['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            # Use 'aplay' or other tools to play the WAV file
            subprocess.run(['aplay', wav_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


# Test the function
input_text = "Hello, this is a test message from ElevenLabs!"
# text_to_speech_with_elevenlabs(
#     input_text=input_text, output_filepath="elevenlabs_testing_autoplay.mp3")
