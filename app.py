from flask import Flask, render_template, jsonify
import detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start')
def start():
    detector.run_thread()
    return "Started"

@app.route('/stop')
def stop():
    detector.stop_detection()
    return "Stopped"

@app.route('/stats')
def stats():
    return jsonify(detector.stats)

if __name__ == '__main__':
    app.run(debug=True)
