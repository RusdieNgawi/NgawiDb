```python
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static', template_folder='.')

# Data film yang sudah dipersonalisasi
MOVIES = [
    { 
        "id": 1, 
        "title": "Ladesh: Suami dari Masa Depan", 
        "year": "2025", 
        "rating": "8.2", 
        "genre": "Sci-Fi / Drama Romantis", 
        "image": "1000168964.png", 
        "description": "Seorang pria dari masa depan kembali ke Ngawi tahun 2025 untuk mencegah suaminya meninggal." 
    },
    { 
        "id": 9, 
        "title": "Kehitaman: The Verdict", 
        "year": "2025", 
        "rating": "7.5", 
        "genre": "Legal Drama", 
        "image": "1000168965.png", 
        "description": "Perdebatan sengit di meja hijau mengenai hak asasi para penganut aliran 'Hitam' di mata hukum negara." 
    }
    # Film lainnya akan dirender melalui list tabel di frontend
]

@app.route('/')
def index():
    return render_template('index.html', movies=MOVIES)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)

```
