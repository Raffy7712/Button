import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  Termux button plus ')
print(a+'\t  UP,Down,right,Left, CTRL ')
print(b+'\t  By:  Weekly Studios')
print(a+'+'*40)
print('\nProses..')
sleep(1)
print(b+'\n[My] Mencari File Asli...')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[My] File Asli Ditemukan')
sleep(1)
print(b+'\n[My] Mengedit File Asli...')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[My] processing  !')
sleep(1)
print(b+'\n[My] Menyimpan File')
sleep(2)
os.system('termux-reload-settings')
print(a+'[My] Peogram Berhasil Di Jalankan !! ^^'+c+'\n\n[My] Selamat Anda Berhasil*\n\n')
