from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    lyrics = [
    (0, "Vamos pa' la playa, pa' curarte el alma"),
    (5, "Cierra la pantalla, abre la Medalla"),
    (10, "Todo el mar Caribe, viendo tu cintura"),
    (15, "Tú le coqueteas, tú eres buscabullas y me gusta"),
    (20, "Lento y contento, cara al viento"),
    (25, "Lento y contento, cara al viento")
]
    html_lyrics = ''.join(f'<p class="lyric-line">{line}</p>' for line in lyrics)

    return f"""
    <!DOCTYPE html>
    <html><head>
    <style>
    body {{background:#111;color:#fff;font-family:sans-serif;padding:50px}}
    .lyrics-container {{height:80vh;overflow:auto;padding:20px;border:2px solid #fff}}
    .lyric-line {{opacity:0.4;margin:10px 0;transition:opacity 0.3s,transform 0.3s}}
    .lyric-line.active {{opacity:1;font-size:1.5em;color:#00ff88}}
    </style>
    </head><body>
    <div class="lyrics-container">{html_lyrics}</div>
    <script>
    const lines=document.querySelectorAll('.lyric-line');let index=0;
    function highlightNextLine(){{
      if(index>0)lines[index-1].classList.remove('active');
      if(index<lines.length){{
        lines[index].classList.add('active');
        lines[index].scrollIntoView({{behavior:'smooth',block:'center'}});
        index++;setTimeout(highlightNextLine,2000);
      }}
    }}highlightNextLine();
    </script>
    </body></html>
    """
