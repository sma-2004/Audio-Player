from flask import Flask, send_from_directory

app = Flask(__name__)

# Define the directory where your audio files are located
audio_directory = 'audio/'

# Serve audio files
@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory(audio_directory, filename)

# Define the directory where your thumbnail images are located
thumbnail_directory = 'photo/'

# Serve thumbnail images
@app.route('/photo/<path:filename>')
def serve_thumbnail(filename):
    return send_from_directory(thumbnail_directory, filename)


if __name__ == '__main__':
    app.run(debug=True)
