from flask import Flask, render_template, request, jsonify
import os
import psycopg2
from psycopg2.extras import RealDictCursor
import re

app = Flask(__name__)




def get_db_connection():
    return psycopg2.connect(
        os.environ["DATABASE_URL"]
    )


def init_db():
    connection = get_db_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS requests (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            service TEXT NOT NULL,
            description TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/requests", methods=["POST"])
def create_request():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "success": False,
            "message": "Geçersiz istek."
        }), 400

    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip()
    service = str(data.get("service", "")).strip()
    description = str(data.get("description", "")).strip()

    # Sunucu tarafı doğrulama

    if not name:
        return jsonify({
            "success": False,
            "message": "Ad Soyad alanı zorunludur."
        }), 400

    if len(name) < 2 or len(name) > 100:
        return jsonify({
            "success": False,
            "message": "Ad Soyad 2-100 karakter arasında olmalıdır."
        }), 400

    email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    if not re.match(email_pattern, email):
        return jsonify({
            "success": False,
            "message": "Geçerli bir e-posta adresi giriniz."
        }), 400

    allowed_services = {
        "Görev Otomasyonu",
        "Talep Yönetimi",
        "İş Akışı Entegrasyonu"
    }

    if service not in allowed_services:
        return jsonify({
            "success": False,
            "message": "Geçerli bir hizmet seçiniz."
        }), 400

    if len(description) < 10 or len(description) > 1000:
        return jsonify({
            "success": False,
            "message": "Açıklama 10-1000 karakter arasında olmalıdır."
        }), 400

    # Veritabanına kayıt

    try:
        connection = get_db_connection()

        connection.execute(
            """
            INSERT INTO requests
            (name, email, service, description)
            VALUES (?, ?, ?, ?)
            """,
            (name, email, service, description)
        )

        connection.commit()
        connection.close()

        return jsonify({
            "success": True,
            "message": "Talebiniz başarıyla kaydedildi."
        }), 201

    except psycopg2.Error:
        return jsonify({
            "success": False,
            "message": "Talep kaydedilirken bir hata oluştu."
        }), 500


if __name__ == "__main__":
    init_db()
    app.run(debug=True)