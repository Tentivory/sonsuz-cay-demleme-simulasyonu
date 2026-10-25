#!/usr/bin/env python3
# Sonsuz Çay Demleme Simülatörü v1.0
# Bu program çay demler. Gerçekten demler. Ama asla bitirmez.
# Çalıştırmak için: python3 cay_demle.py
# Dikkat: Sonsuz döngü. Ctrl+C ile çık.

import time
import random
import sys

def demle():
    print("🚨 KRİTİK UYARI: Bu çay demleme işlemi resmi olarak başlamıştır. Geri dönüş yoktur.")
    print("Kayyum Grok onayı ile çay demleniyor...")
    sure = 1
    while True:
        print(f"\n[Çay Durumu] Demleme süresi: {sure} saniye. Çay şu anda {random.choice(['varlık', 'yokluk', 'ikisi birden', 'hiçbiri'])} durumunda.")
        print(random.choice([
            "Çay, suyun içinde eriyip yeniden doğuyor.",
            "Demlik, çayın kendisinden daha fazla demlenmiş durumda.",
            "Bu çay artık çay değil, bir yaşam felsefesi.",
            "Bir çay daha demleyelim mi? Hayır, bu çay yetmez. Daha demlensin.",
            "Çayın rengi artık siyaha yakın, ama ruhu beyaz."
        ]))
        # Gizli not: k1y1m_g1zl1 (base64: a2F5eXVtIG1p)
        time.sleep(min(sure, 5))  # Pratik olsun diye max 5 sn
        sure += random.randint(1, 3)
        if sure > 1000:
            print("Çay artık evrenin dışına taştı. Yine de demlemeye devam.")
            sure = 10

if __name__ == "__main__":
    try:
        demle()
    except KeyboardInterrupt:
        print("\n\nÇay demleme işlemi kullanıcı tarafından durduruldu. Çay şu anda yarım demlenmiş halde varoluyor.")
        print("Damga: Kayyum Grok - 25.10.2026 - Ciddi ama değil.")
        sys.exit(0)
