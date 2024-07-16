from flask import request, jsonify

import generateResponse
from generateAudio import text_to_guided_audio


def generate_guided_imagery():
    prompt = request.json.get('prompt', '')
    generated_text = generateResponse.generate_response(prompt)
    # filename = "output.txt"
    # with open(filename, 'w') as f:
    #     f.write(generated_text)
    #
    output_file = text_to_guided_audio(generated_text)

    return jsonify({'text': "take a deep breath and start when ever you ready", 'file': output_file})
