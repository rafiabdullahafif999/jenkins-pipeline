from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Inisialisasi Database SQLite Sederhana
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL
        )
    ''')
    cursor.execute("INSERT INTO logs (message) VALUES ('Aplikasi berhasil terhubung ke Database!')")
    conn.commit()
    conn.close()

# Jalankan inisialisasi tabel saat aplikasi start
init_db()

@app.route('/')
def hello():
    # Ambil data dari database untuk membuktikan koneksi berjalan
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM logs ORDER BY id DESC LIMIT 1")
    db_message = cursor.fetchone()[0]
    conn.close()

    return f"Halo dari Flask + Docker + Jenkins! <br> Status DB: <b>{db_message}</b>"

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    payload = request.get_json(silent=True)
    print("Webhook diterima dari GitHub")
    return "Webhook received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
