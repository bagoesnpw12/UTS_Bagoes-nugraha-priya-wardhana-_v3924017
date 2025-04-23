import pandas as pd
import matplotlib.pyplot as plt

# 1. Membaca data
data = pd.read_csv('data_pasien2.csv', delimiter=';')

# 2. Menghitung TP, FP, TN, FN
TP = len(data[(data['Hasil_Tes'] == 'Positif') & (data['Menderita_Penyakit'] == 'Ya')])
FP = len(data[(data['Hasil_Tes'] == 'Positif') & (data['Menderita_Penyakit'] == 'Tidak')])
TN = len(data[(data['Hasil_Tes'] == 'Negatif') & (data['Menderita_Penyakit'] == 'Tidak')])
FN = len(data[(data['Hasil_Tes'] == 'Negatif') & (data['Menderita_Penyakit'] == 'Ya')])
PPV = TP / (TP + FP)
print(f"a. Probabilitas pasien benar-benar menderita penyakit jika hasil tes positif: {PPV:.2%}")
NPV = TN / (TN + FN)
print(f"b. Probabilitas pasien tidak terkena penyakit jika hasil tes negatif: {NPV:.2%}")
labels = ['Positif', 'Negatif']
counts = [len(data[data['Hasil_Tes'] == 'Positif']), len(data[data['Hasil_Tes'] == 'Negatif'])]
plt.figure(figsize=(8, 6))
plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
plt.title('Distribusi Hasil Tes Medis')
plt.axis('equal') 
plt.show()

print("\nTabel Ringkasan:")
summary = pd.DataFrame({
    'Kategori': ['True Positive', 'False Positive', 'True Negative', 'False Negative'],
    'Jumlah': [TP, FP, TN, FN]
})
print(summary)