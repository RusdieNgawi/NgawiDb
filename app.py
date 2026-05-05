```python
from flask import Flask, render_template, send_from_directory
import os

# Karena app.py ada di root, kita set template_folder dan static_folder ke root dan /static
app = Flask(__name__, 
            template_folder='.', 
            static_folder='static')

MOVIES = [
    { 
        "id": "ladesh-2025", 
        "title": "Ladesh: Suami dari Masa Depan", 
        "year": "2025", 
        "genre": "Sci-Fi / Drama Romantis", 
        "image": "1000168964.png", 
        "description": "Seorang pria dari masa depan kembali ke Ngawi tahun 2025 untuk mencegah pernikahan yang akan menghancurkan tatanan dunia." 
    },
    { 
        "id": "kehitaman-2025", 
        "title": "Kehitaman: The Verdict", 
        "year": "2025", 
        "genre": "Legal Drama", 
        "image": "1000168965.png", 
        "description": "Perdebatan sengit di meja hijau mengenai hak asasi para penganut aliran 'Hitam' di mata hukum negara." 
    }
]

KATALOG = [
    {"id": "pesukian-2026", "title": "Jangan Bawa Aku!: Pesukian Massal", "year": "2026", "genre": "Tragedi / Horror", "rating": "8.1"},
    {"id": "500days-2009", "title": "(500) Days Of Imut", "year": "2009", "genre": "Romance / Coming-of-Age", "rating": "8.0"},
    {"id": "zonahitam-2026", "title": "Zona Hitam", "year": "2026", "genre": "Action / Survival Horror", "rating": "7.9"},
    {"id": "jomokerto-2023", "title": "Jomokerto: Kota Ghaib", "year": "2023", "genre": "Urban Legend", "rating": "7.1"}
]

@app.route('/')
def index():
    # Flask akan mencari index.html langsung di root karena template_folder='.'
    return render_template('index.html', featured=MOVIES, catalog=KATALOG)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# Sangat penting bagi Vercel untuk mengenali objek app
app = app

if __name__ == '__main__':
    app.run(debug=True)

```
