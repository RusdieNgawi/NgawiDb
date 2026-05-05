```python
from flask import Flask, render_template, send_from_directory
import os

# Konfigurasi path agar aman di serverless environment (Vercel)
# Kita tentukan folder templates dan static secara eksplisit
base_dir = os.path.dirname(os.path.abspath(__file__))
# Naik satu level ke root
root_dir = os.path.dirname(base_dir)

app = Flask(__name__, 
            template_folder=os.path.join(root_dir, 'templates'),
            static_folder=os.path.join(root_dir, 'static'))

MOVIES = [
    { 
        "id": "ladesh-2025", 
        "title": "Ladesh: Suami dari Masa Depan", 
        "year": "2025", 
        "genre": "Sci-Fi / Drama Romantis", 
        "image": "1000168964.png", 
        "description": "Seorang pria dari masa depan kembali ke Ngawi tahun 2025 untuk mencegah pernikahan." 
    },
    { 
        "id": "kehitaman-2025", 
        "title": "Kehitaman: The Verdict", 
        "year": "2025", 
        "genre": "Legal Drama", 
        "image": "1000168965.png", 
        "description": "Perdebatan sengit mengenai hak asasi faksi 'Hitam' di mata hukum." 
    }
]

KATALOG = [
    {"id": "pesukian-2026", "title": "Jangan Bawa Aku!: Pesukian Massal", "year": "2026", "genre": "Tragedi / Horror", "rating": "8.1"},
    {"id": "500days-2009", "title": "(500) Days Of Imut", "year": "2009", "genre": "Romance", "rating": "8.0"}
]

@app.route('/')
def index():
    # Mencari index.html di folder /templates
    return render_template('index.html', featured=MOVIES, catalog=KATALOG)

# Route untuk melayani file gambar dari folder /static
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# Diperlukan untuk Vercel agar mengenali variabel app
app = app

```
