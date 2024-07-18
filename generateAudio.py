import os
import io
import re
import random
from google.cloud import texttospeech
from pydub import AudioSegment

# Set Google application credentials for Text-to-Speech API access
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "third-shade-425412-m6-aa7deb7f302e.json"


class TextToSpeech:
    """
    A class to convert text to speech using Google's Text-to-Speech API.
    """

    def __init__(self, text):
        """
        Initializes the TextToSpeech instance with the provided text.

        Parameters:
            text (str): The text to be converted to speech.
        """
        self.client = texttospeech.TextToSpeechClient()
        self.text = text

    def get_audio(self):
        """
        Generates an audio file from the text.

        Returns:
            AudioSegment: The generated audio segment.
        """
        # Setup the synthesis input and voice parameters
        synthesis_input = texttospeech.SynthesisInput(text=self.text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Wavenet-C",  # Using a specific Wavenet female voice
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16,  # WAV format
            pitch=-3.0,  # Lower pitch for calmness
            speaking_rate=0.85,  # Slower speaking rate for calmness
            volume_gain_db=1.0  # Slight volume gain to ensure clarity
        )

        # Request speech synthesis
        response = self.client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

        # Load the audio in memory
        audio_stream = io.BytesIO(response.audio_content)
        audio = AudioSegment.from_file(audio_stream, format="wav")

        # Save the audio to a file
        return audio


def text_to_guided_audio(text, relaxing_music_path='relaxing_music.wav'):
    # Define the durations for the pauses (in milliseconds)
    pauses = {
        "(PAUSE, 5 SEC)": 5000,
        "(PAUSE, 15 SEC)": 15000,
        "(PAUSE, 20 SEC)": 20000,
        "(PAUSE, 25 SEC)": 20000,
        "(PAUSE, 30 SEC)": 30000,
        "(PAUSE, 10 SEC)": 10000
    }

    fade_duration = 2000  # Duration of fade-out in milliseconds

    segments = re.split(r'\(PAUSE, [0-9]+ SEC\)', text)
    pause_markers = re.findall(r'\(PAUSE, [0-9]+ SEC\)', text)

    speech_segments = []
    for i, segment in enumerate(segments):
        if segment.strip():
            tts = TextToSpeech(segment.strip())
            speech_segments.append(tts.get_audio())

    relaxing_music = AudioSegment.from_file(relaxing_music_path)

    final_audio = speech_segments[0]
    for i in range(len(pause_markers)):
        pause_duration = pauses[pause_markers[i]]
        music_segment = relaxing_music[:pause_duration].fade_out(fade_duration)
        final_audio += music_segment
        if i + 1 < len(speech_segments):
            final_audio += speech_segments[i + 1]

    output_file = "guided_imagery_with_music.wav"
    final_audio.export(output_file, format="wav")
    return output_file




