import streamlit as st

st.set_page_config(
    page_title='multipage app',
    page_icon='M'
)

st.title(' Rangkaian listrik')
st.sidebar.success('select a page above.')


st.subheader("Pengertian rangkaian listrik")


st.write("  Rangkaian Listrik adalah sebuah rangkaian atau jalur yang dibuat, sehingga elektron bisa mengalir dari sumber voltase atau arus listrik. Proses perpindahan elektron itulah yang kita kenal sebagai listrik, elemen yang membaut barang-barang elektronik bisa digunakan sesuai dengan fungsinya.")
st.write("  Ada dua jenis atau tipe rangkaian yang biasa digunakan untuk saat ini, yakni rangkaian seri dan juga rangkaian paralel. Rangkaian seri dan paralel tersebut bisa dikombinasikan sehingga menjadi rangkaian listrik campuran.")

st.subheader("Rangkaian seri")
st.write("  Dalam rangkaian seri, hanya ada satu baris arus listrik, yang bagian rangkaiannya dipasang secara berderet atau beruntutan tanpa adanya percabangan. Rangkaian yang satu ini, akan terbentuk apabila dua buah atau lebih komponen elektronika dihubungkan secara berderet.")
st.write("  Besaran hambatan listrik (gambar b) di dalam rangkaian, sama dengan jumlah pada masing-masing hambatan. Untuk tipe yang satu ini, rangkaian listrik rumus adalah: Rs = R₁ + R₂ + R₃")

st.subheader("Rangkaian Pararel")
st.write("Rangkaian paralel merupakan rangkaian yang dibentuk jika dua buah lampu atau lebih dihubungkan secara berjajar, sehingga disebut juga sebagai rangkaian bercabang. Arus yang diterima oleh setiap cabang, lebih besar dibandingkan arus dalam rangkaian seri, hal ini akan membuat lampu mampu menyala lebih terang.")
st.write("  Rangkaian lampu di rumah, di kantor, dan juga lampu lalu lintas, adalah contoh rangkaian listrik paralel di kehidupan sehari-hari. Apabila arus lebih banyak mengalir dari sumber (penjumlahan tiap cabang), maka resistensi atau perlawanan total pada rangkaian paralel akan jauh lebih kecil daripada seri")
st.write("  Bisa dibilang jika keuntungan dan kerugian rangkaian paralel ini adalah kebalikan dari rangkaian seri, jadi rangkaian paralel penggambaran adalah Rt = 1/(1/R1 + 1/R2 + 1/R3)")

st.title(" ARUS, TEGANGAN DAN HAMBATAN")
st.subheader("Pengertian Arus")
st.write("  Arus listrik adalah laju aliran muatan listrik melewati suatu titik dalam suatu konduktor. Arus listrik (arus listrik konvensional) mengalir dari kutub positif ke nagatif. Namun, arus elektron mengalir dari kutub negatif ke kutub positif. Arus listrik dinyatakan dengan simbol “I”. Satuan Internasional dari arus adalah Ampere (A), yang merupakan aliran muatan listrik melintasi konduktor dengan kecepatan satu coulomb per detik. Berikut ini adalah rumus yang digunakan untuk mencari besarnya arus listrik:")
st.write("I = V / R")
st.subheader("HAMBATAN")
st.write("  Hambatan listrik adalah ukuran sejauh mana suatu objek menentang aliran arus listrik. Hambatan listrik mempunyai dua sifat, yaitu yang pertama, semakin panjang/besar bahan yang digunakan sebagai konduktor maka semakin besar nilai hambatannya. Kedua, semakin pendek/kecil bahan yang digunakan sebagai konduktor maka semakin kecil nilai hambatannya. Hambatan listrik dinyatakan dengan simbol “R”, dan Satuan Internasional dari hambatan adalah Ohm (Ω). Berikut ini adalah rumus untuk mencari hambatan listrik:")
st.write("R = V / I")
st.subheader("TEGANGAN")
st.write("  Tegangan listrik adalah perbedaan potensial listrik per satuan muatan antara dua titik dalam medan listrik. Atau dapat juga diartikan tegangan adalah besarnya jumlah energi yang dibutuhkan untuk memindahkan unit muatan listrik dari satu tempat ke tempat lainnya. Tegangan dinyatakan menggunakan simbol V. Satuan Internasional dari tegangan adalah Volt (V). Berikut adalah rumus yang digunakan untuk mencari tegangan listrik:")
st.write("V = I x R")

st.text("Sekian Terima Kasih")

