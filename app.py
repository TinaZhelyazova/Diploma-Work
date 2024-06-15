from flask import Flask, request, render_template, send_file
from midi_generator import Track
from tabs_reading import Tabs
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_midi', methods=['POST'])
def generate_midi():
    file = request.files['file']
    tempo = request.form['tempo']

    if not tempo.isdigit():
        tempo = 100
    else:
        tempo = int(tempo)

    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

        try:
            tabs = Tabs(file_path)
            tabs.preprocess()
            tabs.convertNotes()

            output_track = Track(tempo)
            output_track.midiGenerator(tabs.a)

            output_filename = "output.mid"
            return send_file(output_filename, as_attachment=True)
        except Exception as e:
            return str(e)
    return "File not provided", 400


if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
