from flask import Flask, render_template, request, redirect, url_for
import youtube_dl

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
from flask_bootstrap import Bootstrap

Bootstrap(app)

def download_video(url):
    ydl_opts = {
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        if video_url:
            download_video(video_url)
            return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
