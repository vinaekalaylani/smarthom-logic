print("=== Simulasi Keputusan AI di Rumah Pintar ===")
print("Masukkan kondisi berikut:")

orang = input("Apakah ada orang di rumah? (y/n): ").strip().lower()
P = orang == 'y'

suhu = input("Apakah suhu di atas 30°C? (y/n): ").strip().lower()
Q = suhu == 'y'

operator = input("Gunakan logika apa? (and/or): ").strip().lower()

if operator == 'and':
    hasil = P and Q
    simbol = '∧'
elif operator == 'or':
    hasil = P or Q
    simbol = '∨'
else:
    print("Operator tidak dikenal. Harus 'and' atau 'or'.")
    hasil = None

print("\n=== Hasil Evaluasi ===")
if hasil is not None:
    print(f"Logika: {P} {simbol} {Q} = {hasil}")
    
    if hasil:
        print("Keputusan: ✅ AC DINYALAKAN")
    else:
        print("Keputusan: ❌ AC TIDAK DINYALAKAN")
