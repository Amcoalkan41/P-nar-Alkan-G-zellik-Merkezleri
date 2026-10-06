from flask import Flask

app = Flask(__name__)


@app.route("/")
def guzellik_merkezi():
    # Annenin gözlerini yerinden fırlatacak şık ve kurumsal güzellik merkezi tasarımı (HTML/CSS/JS)
    return """
    <html>
    <head>
        <title>Pınar Alkan Güzellik Merkezi</title>
        <style>
            body { background-color: #faf6f6; color: #333333; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; padding: 0; margin: 0; }
            header { background: linear-gradient(135deg, #d4a373, #faedcd); padding: 40px; box-shadow: 0 5px 20px rgba(0,0,0,0.1); }
            h1 { color: #5c3d2e; font-size: 42px; margin: 0; font-weight: bold; letter-spacing: 1px; text-shadow: 1px 1px 2px rgba(0,0,0,0.1); }
            p.subtitle { color: #8b5e3c; font-size: 18px; font-style: italic; margin-top: 10px; font-weight: 500; }
            .container { max-width: 1200px; margin: 40px auto; padding: 0 20px; }
            h2 { color: #5c3d2e; border-bottom: 2px solid #d4a373; padding-bottom: 10px; margin-top: 40px; font-size: 28px; }
            .grid { display: flex; justify-content: center; gap: 25px; flex-wrap: wrap; margin-top: 20px; }
            .kart { background-color: white; border: 1px solid #e6ccb2; border-radius: 15px; padding: 25px; width: 260px; box-shadow: 0px 10px 25px rgba(212,163,115,0.15); transition: all 0.3s ease; }
            .kart:hover { transform: translateY(-5px); box-shadow: 0px 15px 30px rgba(212,163,115,0.3); border-color: #b5828c; }
            .kart-baslik { font-size: 22px; font-weight: bold; color: #5c3d2e; margin-bottom: 15px; }
            .kart-detay { color: #666666; font-size: 15px; line-height: 1.6; margin-bottom: 15px; }
            .fiyat { font-size: 24px; color: #b5828c; font-weight: bold; margin: 15px 0; }
            .buton { background: linear-gradient(135deg, #d4a373, #b5828c); color: white; border: none; padding: 12px 24px; font-size: 14px; font-weight: bold; border-radius: 25px; cursor: pointer; text-transform: uppercase; width: 100%; transition: 0.3s; }
            .buton:hover { background: linear-gradient(135deg, #b5828c, #d4a373); }
            footer { margin-top: 80px; background-color: #5c3d2e; color: #faedcd; padding: 30px 20px; font-size: 14px; }
        </style>
        <script>
            function randevuAl(hizmetAdi, fiyat) {
                alert("✨ PINAR ALKAN GÜZELLİK MERKEZİ ✨\\n\\n" + hizmetAdi + " için ön rezervasyon talebi oluşturuldu!\\nFiyatlandırma: " + fiyat + "\\n\\nKaan Alkan siber altyapısı ile salon otomasyonu devrededir.");
            }
        </script>
    </head>
    <body>
        <header>
            <h1>✨ PINAR ALKAN GÜZELLİK MERKEZİ</h1>
            <p class="subtitle">Profesyonel Bakım, Medikal Estetik & Tırnak Tasarım Sarayı</p>
        </header>

        <div class="container">
            <!-- HİZMETLER VE FİYATLANDIRMA -->
            <h2>💅 Tırnak & Pedikür Özel Paketleri</h2>
            <div class="grid">
                <!-- 1. Paket -->
                <div class="kart">
                    <div class="kart-baslik">Protez Tırnak VIP</div>
                    <div class="kart-detay">✨ Jel Sistem Protez<br>🎨 Kalıcı Oje Dahil<br>💎 Özel Nail Art Tasarımı<br>⏱️ Süre: 90 Dakika</div>
                    <div class="fiyat">1.250 TL</div>
                    <button class="buton" onclick="randevuAl('Protez Tırnak VIP', '1.250 TL')">Randevu Al</button>
                </div>

                <!-- 2. Paket -->
                <div class="kart">
                    <div class="kart-baslik">Medikal Pedikür</div>
                    <div class="kart-detay">🦶 Sağlık Odaklı Bakım<br>🌿 Topuk Sertlik Giderme<br>💧 Yoğun Nemlendirici Masaj<br>⏱️ Süre: 60 Dakika</div>
                    <div class="fiyat">950 TL</div>
                    <button class="buton" onclick="randevuAl('Medikal Pedikür', '950 TL')">Randevu Al</button>
                </div>

                <!-- 3. Paket -->
                <div class="kart">
                    <div class="kart-baslik">Kalıcı Oje & Manikür</div>
                    <div class="kart-detay">💅 Kusursuz Manikür<br>🔥 4 Hafta Kalıcı Parlaklık<br>🛡️ Tırnak Güçlendirici Vitamin<br>⏱️ Süre: 45 Dakika</div>
                    <div class="fiyat">700 TL</div>
                    <button class="buton" onclick="randevuAl('Kalıcı Oje & Manikür', '700 TL')">Randevu Al</button>
                </div>
            </div>

            <!-- UZMANLARIMIZ SEKMESİ -->
            <h2>👩‍⚕️ Alanında Uzman Kadromuz</h2>
            <div class="grid">
                <!-- 1. Uzman -->
                <div class="kart" style="width: 350px;">
                    <div class="kart-baslik" style="color: #b5828c;">👑 Pınar Alkan</div>
                    <div class="kart-detay" style="font-size: 16px; font-weight: 500;">
                        🏆 Kurucu & Baş Güzellik Uzmanı<br><br>
                        Medikal estetik, profesyonel cilt analizi ve ileri seviye tırnak mimarisi alanlarında uzmanlaşmış, sektörün öncü lideri.
                    </div>
                </div>
            </div>
        </div>

        <footer>
            <p>© 2026 Pınar Alkan Güzellik Merkezi. Tüm Hakları Saklıdır.</p>
            <p style="font-size: 11px; color: #e6ccb2; margin-top: 10px;">Alkan Global Software Holding tarafından nizamı kodlanmıştır.</p>
        </footer>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run()
