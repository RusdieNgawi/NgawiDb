```python
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='.', static_folder='static')

# Data Film Lengkap (Sudah Tayang)
# Menambahkan field 'image' untuk referensi poster di static folder
MOVIES_TAYANG = [
    {
        "title": "Ladesh: Suami dari Masa Depan", 
        "year": "2025", 
        "rating": "8.2", 
        "genre": "Sci-Fi / Drama Romantis", 
        "desc": "Seorang pria dari masa depan kembali ke Ngawi tahun 2025 untuk mencegah pernikahan yang akan menghancurkan tatanan dunia.",
        "image": "1000168964.png"
    },
    {
        "title": "Kehitaman: The Verdict", 
        "year": "2025", 
        "rating": "7.5", 
        "genre": "Legal Drama", 
        "desc": "Perdebatan sengit di meja hijau mengenai hak asasi para penganut aliran 'Hitam' di mata hukum negara.",
        "image": "1000168965.png"
    },
    {"title": "Jangan Bawa Aku!: Pesukian Massal", "year": "2026", "rating": "8.1", "genre": "Tragedi / Psychological Horror", "desc": "Kisah pilu para Jomokers yang diculik dan dipaksa menjalani ritual pembersihan identitas oleh kelompok radikal.", "image": ""},
    {"title": "(500) Days Of Imut", "year": "2009", "rating": "8.0", "genre": "Romance / Coming-of-Age", "desc": "Memoar 500 hari perjalanan cinta seorang pemuda dengan sosok ikonik bernama Imut yang berakhir penuh pelajaran hidup.", "image": ""},
    {"title": "Zona Hitam", "year": "2026", "rating": "7.9", "genre": "Action / Survival Horror", "desc": "Ngawi diisolasi setelah wabah misterius mengubah penduduknya menjadi entitas agresif. Sekelompok penyintas harus bertahan di pusat kota.", "image": ""},
    {"title": "Pesan Perang: Antara Jomok dan Suki", "year": "TBA", "rating": "7.9", "genre": "War / Epic", "desc": "Dokumentasi besar tentang konflik perebutan wilayah kekuasaan dan ideologi antara faksi Hitam dan faksi Putih di tanah Ngawi.", "image": ""},
    {"title": "Kehitaman 2: The Verdict", "year": "2026", "rating": "7.8", "genre": "Legal Thriller / Crime", "desc": "Kelanjutan persidangan paling kontroversial yang mengungkap keterlibatan pejabat tinggi dalam skandal korupsi ritual.", "image": ""},
    {"title": "Pengepungan Di Bukit Ngawi", "year": "TBA", "rating": "7.7", "genre": "War Drama / Art-house", "desc": "Sebuah metafora perjuangan sepi lima prajurit terakhir yang bertahan di atas bukit saat dikhianati oleh sekutu mereka.", "image": ""},
    {"title": "Agak Ngawi 2: Menyala Boolku", "year": "2025", "rating": "7.6", "genre": "Comedy / Adventure", "desc": "Empat sekawan kembali dengan bisnis baru yang lebih absurd, namun kali ini mereka harus berhadapan dengan masalah pencernaan yang mistis.", "image": ""},
    {"title": "Another Life: Adriana", "year": "TBA", "rating": "7.5", "genre": "Biopic / Melodrama", "desc": "Mengungkap masa lalu kelam Adriana sebelum menjadi pemilik Barbershop, tentang kehilangan dan pencarian jati diri.", "image": ""},
    {"title": "Kutukan Hitam: The Black Conjuring", "year": "2026", "rating": "7.5", "genre": "Supernatural Horror", "desc": "Sebuah keluarga pindah ke rumah tua di pinggiran Jomokerto yang ternyata merupakan bekas tempat pemujaan kuno.", "image": ""},
    {"title": "Para Perodok", "year": "2026", "rating": "7.4", "genre": "Action / Heist", "desc": "Sekelompok pemuda ahli menyusun rencana besar untuk mengambil kembali aset faksi yang disita oleh pihak berwajib.", "image": ""},
    {"title": "Penghitaman Abadi", "year": "2017", "rating": "7.4", "genre": "Dark Fantasy", "desc": "Legenda tentang awal mula kegelapan abadi yang menyelimuti wilayah Ngawi ribuan tahun silam.", "image": ""},
    {"title": "13 Bom di Banyumas", "year": "TBA", "rating": "7.3", "genre": "Action Thriller", "desc": "Satuan anti-teror berpacu dengan waktu untuk menjinakkan 13 bom yang tersebar di titik vital wilayah Banyumas.", "image": ""},
    {"title": "Monyet Ijo Banyumas: Legenda Tanah Banyumas", "year": "TBA", "rating": "7.2", "genre": "Folklore / Mystery", "desc": "Penelusuran sejarah tentang entitas primata hijau yang menjadi penjaga hutan larangan di Banyumas.", "image": ""},
    {"title": "Agak Ngawi", "year": "2024", "rating": "7.2", "genre": "Comedy / Slice of Life", "desc": "Kisah keseharian pemuda Ngawi yang mencoba peruntungan menjadi content creator namun selalu berakhir sial.", "image": ""},
    {"title": "BetterCall Fuad", "year": "TBA", "rating": "7.2", "genre": "Black Comedy / Crime", "desc": "Fuad, seorang makelar segala urusan, mencoba membersihkan namanya setelah terlibat kasus pencucian uang di Barbershop.", "image": ""},
    {"title": "Pengocok: Sang Detektif Ngawi", "year": "TBA", "rating": "7.1", "genre": "Mystery / Neo-noir", "desc": "Seorang detektif swasta dengan metode penyelidikan yang aneh mencoba memecahkan kasus hilangnya stok pomade hitam.", "image": ""},
    {"title": "Jomokerto: Kota Ghaib", "year": "2023", "rating": "7.1", "genre": "Urban Legend / Thriller", "desc": "Sekelompok mahasiswa terjebak di sebuah kota yang tidak ada di peta, di mana waktu berhenti berputar.", "image": ""},
    {"title": "Suki: Asal Usul Di Tanah Ngawi", "year": "2026", "rating": "7.1", "genre": "Mockumentary / Propaganda", "desc": "Versi faksi putih mengenai sejarah kemunculan mereka, yang diklaim sebagai pembawa cahaya di Ngawi.", "image": ""},
    {"title": "Pengabdi Amba 1", "year": "TBA", "rating": "7.0", "genre": "Horror", "desc": "Sebuah keluarga diteror oleh sosok kakek tua yang menuntut janji dari masa lalu yang belum ditepati.", "image": ""},
    {"title": "Sekawan Jomok", "year": "2024", "rating": "6.9", "genre": "Comedy / Friendship", "desc": "Perjalanan liburan empat sahabat ke Jomokerto yang berubah menjadi kacau karena salah paham dengan warga lokal.", "image": ""},
    {"title": "Kontrak Abadi: Para Jomok", "year": "TBA", "rating": "6.8", "genre": "Drama / Thriller", "desc": "Kisah tentang perjanjian mengikat yang harus ditandatangani oleh setiap anggota baru faksi demi kesetiaan mutlak.", "image": ""},
    {"title": "28 Februari: Teror Suki Liar", "year": "TBA", "rating": "6.7", "genre": "Slasher / Horror", "desc": "Tanggal 28 Februari menjadi malam berdarah ketika kelompok bertopeng putih melakukan sweeping besar-besaran.", "image": ""},
    {"title": "Ambavin: Sebelum 7 Hari", "year": "2024", "rating": "6.7", "genre": "Supernatural Thriller", "desc": "Seseorang mendapatkan pesan misterius bahwa ia hanya memiliki waktu 7 hari sebelum entitas Ambavin menjemputnya.", "image": ""},
    {"title": "Pabrik Muwani", "year": "2025", "rating": "6.6", "genre": "Gore / Industrial Horror", "desc": "Rahasia mengerikan di balik pabrik pengolahan daging yang pekerjanya dilarang keluar dari area pabrik.", "image": ""},
    {"title": "Amba In The Cell", "year": "2026", "rating": "6.5", "genre": "Prison / Action", "desc": "Amba harus bertahan hidup di dalam penjara dengan keamanan maksimum sambil merencanakan pelarian besar.", "image": ""},
    {"title": "My Muwani", "year": "TBA", "rating": "6.5", "genre": "Drama / Romance", "desc": "Hubungan cinta terlarang antara seorang mandor pabrik dengan salah satu buruh di tengah tekanan kerja yang keras.", "image": ""},
    {"title": "Adriana: Barbershop Hitam", "year": "TBA", "rating": "6.4", "genre": "Mystery / Drama", "desc": "Kejadian-kejadian aneh yang dialami pelanggan yang mencukur rambut di barbershop milik Adriana saat tengah malam.", "image": ""},
    {"title": "Ambacong 3: Revenge Of Ambacong", "year": "TBA", "rating": "6.4", "genre": "Fantasy / Action", "desc": "Sang monster Ambacong kembali untuk membalas dendam kepada mereka yang telah menyegelnya di dalam botol.", "image": ""},
    {"title": "Jangan: Rodok Aku", "year": "TBA", "rating": "6.3", "genre": "Experimental / Drama", "desc": "Film tentang pencarian jati diri seorang pemuda yang merasa tidak cocok dengan budaya 'Rodok' yang ada.", "image": ""},
    {"title": "Imut Adalah Maut", "year": "TBA", "rating": "6.2", "genre": "Horror Thriller", "desc": "Sosok Imut kembali, namun kali ini bukan untuk dicintai, melainkan untuk menebar teror melalui mimpi.", "image": ""},
    {"title": "Tunggu Aku Di Ngawi", "year": "2026", "rating": "6.1", "genre": "Slow Cinema / Romance", "desc": "Penantian panjang seorang wanita di Stasiun Ngawi untuk kekasihnya yang tak kunjung pulang dari perang faksi.", "image": ""},
    {"title": "Ambarawuhi: Di Desa Penari", "year": "TBA", "rating": "6.0", "genre": "Folk Horror", "desc": "Adaptasi lokal tentang kutukan penari mistis yang menjerat siapa pun yang berani masuk ke desanya.", "image": ""},
    {"title": "Ambaruwo: Legenda Tanah Ngawi", "year": "TBA", "rating": "5.8", "genre": "Mythical / Adventure", "desc": "Pencarian pedang legendaris yang konon bisa mengalahkan entitas hitam paling kuat di Ngawi.", "image": ""},
    {"title": "Teror: Monyet Ijo Banyumas", "year": "TBA", "rating": "5.7", "genre": "Creature Feature", "desc": "Serangan brutal monyet-monyet misterius yang meneror pemukiman warga di pinggiran Banyumas.", "image": ""},
    {"title": "Desa Jomok", "year": "TBA", "rating": "5.5", "genre": "Mystery", "desc": "Seorang jurnalis mencoba mengungkap mengapa semua pria di sebuah desa memiliki perilaku yang seragam.", "image": ""},
    {"title": "Ambalangkung: Datang Main Rodok", "year": "TBA", "rating": "5.5", "genre": "Horror / Comedy", "desc": "Permainan memanggil arwah menggunakan alat cukur rambut yang berakhir dengan kekacauan komedi-horor.", "image": ""},
    {"title": "Ambacong Dendam Pocong", "year": "TBA", "rating": "5.4", "genre": "Low-budget Horror", "desc": "Pocong yang bangkit kembali karena makamnya terinjak oleh seorang pemuda yang sedang lari dari kejaran Suki.", "image": ""},
    {"title": "Si Imut Jembatan Ngawi", "year": "TBA", "rating": "5.0", "genre": "Urban Horror", "desc": "Penampakan sosok putih di jembatan yang sering mengganggu para pengendara motor yang lewat sendirian.", "image": ""},
    {"title": "Tumbal Jembatan Ngawi", "year": "TBA", "rating": "4.7", "genre": "Slasher", "desc": "Pembangunan jembatan yang memerlukan tumbal manusia, memicu serangkaian pembunuhan misterius di lokasi proyek.", "image": ""},
    {"title": "Abadi Nan Jomok", "year": "TBA", "rating": "4.2", "genre": "Experimental Art", "desc": "Film tanpa dialog yang hanya berisi visualisasi abstrak tentang kehampaan jiwa seorang Jomokers.", "image": ""},
]

MOVIES_COMING = [
    {"title": "Pengabdi Amba 3: Origin", "year": "2027", "genre": "Period Horror / Origin Story", "desc": "Mengambil latar waktu abad ke-19, mengungkap bagaimana kontrak pertama dengan entitas Amba terbentuk."},
    {"title": "Sekawan Ngawi: Gunung Kwontol", "year": "27 Mei", "genre": "Comedy / Horror / Adventure", "desc": "Empat sekawan mendaki gunung keramat untuk mencari pesugihan, namun malah terjebak dalam ritual yang sangat konyol."}
]

@app.route('/')
def index():
    return render_template('index.html', tayang=MOVIES_TAYANG, coming=MOVIES_COMING)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)

```
