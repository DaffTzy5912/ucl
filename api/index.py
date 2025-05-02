from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='../public')

@app.route("/calma.mp3")
def get_audio():
    return send_from_directory(app.static_folder, 'calma.mp3')

@app.route("/")
def index():
    lyrics = [
        (0.5, "Vamos pa' la playa, pa' curarte el alma"),
        (4.2, "Cierra la pantalla, abre la Medalla"),
        (8.0, "Todo el mar Caribe, viendo tu cintura"),
        (12.0, "Tú le coqueteas, tú eres buscabullas y me gusta"),
        (16.0, "Lento y contento, cara al viento"),
        (19.0, "Lento y contento, cara al viento")
    ]

    html_lyrics = ''.join(
        f'<p class="lyric-line" data-time="{t}">{line}</p>' for t, line in lyrics
    )

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Calma - Lirik Sinkron</title>
        <style>
            body {{
                background: #0f0f0f;
                color: #fff;
                font-family: sans-serif;
                padding: 40px;
            }}
            audio {{
                width: 100%;
                margin-bottom: 20px;
            }}
            .lyrics-container {{
                height: 70vh;
                overflow-y: auto;
                border: 1px solid #555;
                padding: 20px;
                border-radius: 10px;
                background-color: #1f1f1f;
            }}
            .lyric-line {{
                opacity: 0.4;
                transition: all 0.3s ease;
                font-size: 1em;
                margin: 10px 0;
            }}
            .lyric-line.active {{
                opacity: 1;
                font-size: 1.5em;
                color: #00ffaa;
            }}
        </style>
    </head>
    <body>
        <h1>Calma - Pedro Capó & Farruko</h1>
        <audio id="audio" controls autoplay>
            <source src="/calma.mp3" type="audio/mpeg">
            Browser tidak mendukung audio.
        </audio>
        <div class="lyrics-container">
            {html_lyrics}
        </div>
        <script>
            const audio = document.getElementById('audio');
            const lines = document.querySelectorAll('.lyric-line');

            audio.ontimeupdate = () => {{
                const currentTime = audio.currentTime;
                for (let i = 0; i < lines.length; i++) {{
                    const time = parseFloat(lines[i].dataset.time);
                    const nextTime = (i + 1 < lines.length) 
                        ? parseFloat(lines[i + 1].dataset.time) 
                        : Infinity;

                    if (currentTime >= time && currentTime < nextTime) {{
                        document.querySelectorAll('.active').forEach(e => e.classList.remove('active'));
                        lines[i].classList.add('active');
                        lines[i].scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                        break;
                    }}
                }}
            }};
        </script>
    </body>
    </html>
    """
