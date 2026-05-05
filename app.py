```python
from flask import Flask, render_template, send_from_directory
import os

# Inisialisasi aplikasi
# Vercel mencari variabel bernama 'app'
app = Flask(__name__, 
            static_folder='static', 
            template_folder='.')

# Database lokal film unggulan
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

# Katalog lengkap
KATALOG = [
    {"id": "pesukian-2026", "title": "Jangan Bawa Aku!: Pesukian Massal", "year": "2026", "genre": "Tragedi / Horror", "rating": "8.1"},
    {"id": "500days-2009", "title": "(500) Days Of Imut", "year": "2009", "genre": "Romance / Coming-of-Age", "rating": "8.0"},
    {"id": "zonahitam-2026", "title": "Zona Hitam", "year": "2026", "genre": "Action / Survival Horror", "rating": "7.9"},
    {"id": "pesanperang-tba", "title": "Pesan Perang: Jomok vs Suki", "year": "TBA", "genre": "War / Epic", "rating": "7.9"},
    {"id": "perodok-2026", "title": "Para Perodok", "year": "2026", "genre": "Action / Heist", "rating": "7.4"},
    {"id": "fuad-tba", "title": "BetterCall Fuad", "year": "TBA", "genre": "Black Comedy", "rating": "7.2"},
    {"id": "jomokerto-2023", "title": "Jomokerto: Kota Ghaib", "year": "2023", "genre": "Urban Legend", "rating": "7.1"}
]

@app.route('/')
def index():
    # Mengirim data ke template index.html
    return render_template('index.html', featured=MOVIES, catalog=KATALOG)

# Rute khusus untuk melayani file statis (foto poster) di Vercel
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# Boilerplate untuk menjalankan lokal
if __name__ == '__main__':
    app.run(debug=True)

```
