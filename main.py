from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from keuangan import keuangan_real as kr
from keuangan import dahboard_keuangan_real as dkr
from chatbot_app import parse_keuangan_dari_teks, rekomendasi_hemat
import os

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from keuangan import keuangan_real as kr
from keuangan import dahboard_keuangan_real as dkr
from chatbot_app import parse_keuangan_dari_teks, rekomendasi_hemat
import os

# Perhatikan: instance harus bernama 'app'
app = Flask(__name__, static_folder="catatan/dist", static_url_path="/")
CORS(app)

# ... (semua route API sama seperti sebelumnya) ...

# Penting untuk Vercel: Jangan jalankan app.run() jika dideploy
# Vercel akan menggunakan instance 'app' secara langsung

# Hanya untuk local development
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

app = Flask(__name__, static_folder="catatan/dist", static_url_path="/")
CORS(app)

# === API ENDPOINTS ===
@app.route("/api/transactions", methods=["GET"])
def get_transactions():
    return jsonify(kr.get_semua_transaksi())

@app.route("/api/transactions", methods=["POST"])
def add_transaction():
    data = request.json
    # Jika input dari AI (teks)
    if "teks" in data:
        parsed = parse_keuangan_dari_teks(data["teks"])
        if "error" in parsed:
            return jsonify({"error": parsed["error"]}), 400
        trans = kr.tambah_transaksi(
            parsed["jenis"], parsed["jumlah"], parsed["kategori"], parsed["deskripsi"]
        )
        return jsonify(trans)
    # Jika input manual
    else:
        trans = kr.tambah_transaksi(
            data["jenis"], data["jumlah"], data["kategori"], data.get("deskripsi", "")
        )
        return jsonify(trans)

@app.route("/api/transactions/<int:id>", methods=["DELETE"])
def delete_transaction(id):
    kr.hapus_transaksi(id)
    return jsonify({"status": "deleted"})

@app.route("/api/dashboard", methods=["GET"])
def dashboard():
    return jsonify({
        "ringkasan": dkr.get_ringkasan(),
        "kategori": dkr.get_kategori_breakdown(),
        "prediksi": dkr.prediksi_arus_kas(7)
    })

@app.route("/api/rekomendasi", methods=["GET"])
def get_rekomendasi():
    trans = kr.get_semua_transaksi()
    return jsonify({"saran": rekomendasi_hemat(trans)})

# === SERVE REACT BUILD ===
@app.route("/")
def serve():
    return send_from_directory(app.static_folder, "index.html")

@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
