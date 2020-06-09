Bot ini digunakan untuk membalas pesan otomatis atau auto reply saat pengguna sedang tidak menggunakan telegram

syarat :
pkg install python
pip install telethon
atau
pip3install telethon

Mendapatkan kode API :
•Buka https://my.telegram.org
•Login pake nomor hp yang digunakan untuk akun Telegram
•Masukkan kode OTP yang dikirim ke Telegram/SMS
•Pilih API Development Tools
•API Title terserah mau diisi apa
•Shortname atau nama sesi yang akan aktif, juga bebas mau diisi apa
•Url mau diisi mau nggak juga gak masalah
•Deskripsi isi terserah
•Klik Create Application
•Done, tinggal copy App api_id & App api_hash

Penggunaan :
•nano bot.py
•ubah :
api_id & api_hash (copas yg tadi)
phone (nomor tele ente)
session_file (terserah)
password (isi password ente kalo Two-Step Verificationnya aktif)
message (isi pesan balasan bot)

Run :
•python bot.py
•masukkan nomor tele
•masukkan otp
•Done

*kalo mau exit tinggal terminate/kill session terminalnya, atau Ctrl + C
