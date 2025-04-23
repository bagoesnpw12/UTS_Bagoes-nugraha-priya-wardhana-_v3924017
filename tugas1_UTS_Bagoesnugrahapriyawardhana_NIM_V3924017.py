import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

rata_rata = 12  
jam_per_hari = 12
jumlah_hari = 30
total_jam = jam_per_hari * jumlah_hari

np.random.seed(10) 
data_simulasi = np.random.poisson(lam=rata_rata, size=total_jam)

plt.figure(figsize=(10, 5))
plt.hist(data_simulasi, bins=range(min(data_simulasi), max(data_simulasi) + 1), density=True, alpha=0.6, color='skyblue', label='Simulasi')
x = np.arange(0, max(data_simulasi) + 1)
plt.plot(x, stats.poisson.pmf(x, rata_rata), 'r-', lw=2, label='Distribusi Poisson Teoretis')
plt.title("Distribusi Frekuensi Kedatangan Pelanggan")
plt.xlabel("Jumlah Pelanggan per Jam")
plt.ylabel("Probabilitas")
plt.legend()
plt.grid(True)
plt.show()

prob_tidak_ada = np.mean(data_simulasi == 0)
prob_lebih_dari_10 = np.mean(data_simulasi > 10)

print(f"Probabilitas tidak ada pelanggan dalam 1 jam: {prob_tidak_ada:.4f}")
print(f"Probabilitas lebih dari 10 pelanggan dalam 1 jam: {prob_lebih_dari_10:.4f}")
