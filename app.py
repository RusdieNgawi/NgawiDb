```python
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='.', static_folder='static')

@app.route('/')
def index():
    # Data dikelola di frontend (index.html) agar performa lebih cepat dan interaktif
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)

```
