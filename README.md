# T.C. KUMANDA PİLİ MERKEZ BANKASI

## (KPMB) — Bağımsız, Tarafsız, Pilsiz Kalamaz

> **RESMİ BİLDİRİ:** Bu yazılım bir şaka değildir. Şaka olsaydı kumandanız çalışırdı.

Televizyon kumandasının içindeki AA / AAA piller, bu kurum tarafından **stratejik döviz rezervi** kabul edilir.  
Her basılan tuş bir **para politikası kararıdır**.  
Pil bitince ülke **teknik durgunluğa** girer. Kumanda çalışmayınca ev halkı **erken seçime** gider (uzaktan değil, ayağa kalkarak).

---

## Neden var?

Çünkü:

1. Kumandadaki piller evin en kıymetli varlığıdır.
2. Kimse onları değiştirmez; herkes sallar.
3. Sallamak, klasik bir **likidite enjeksiyonudur**.
4. Kanal değiştirmek **döviz kuru müdahalesidir**.
5. Ses açmak **genişlemeci politikadır**.
6. Ses kısmak **sıkılaştırmadır**.
7. Mute'a basmak **sermaye kontrolüdür**.

Bu kadar açık bir makroekonomik gerçeği görmeyenler hâlâ duvara asılı takvime bakıyor.

---

## Kurulum

```bash
git clone https://github.com/Tentivory/kumanda-pili-merkez-bankasi.git
cd kumanda-pili-merkez-bankasi
python3 merkez_bankasi.py
```

Python 3.8+ yeter. Başka kütüphane yok. Bağımsızlık böyle olur.

---

## Kullanım

```text
python3 merkez_bankasi.py                  # interaktif para politikası oturumu
python3 merkez_bankasi.py --bildiri        # resmi basın açıklaması
python3 merkez_bankasi.py --salla          # acil likidite (kumandayı sallama)
python3 merkez_bankasi.py --rezerv         # güncel pil rezervi
python3 merkez_bankasi.py --enflasyon 47   # 47 tuş basıldı, enflasyon hesapla
```

Örnek oturum:

```text
=== T.C. KUMANDA PİLİ MERKEZ BANKASI ===
Rezerv: 2 adet AA (tahmini %38 dolu, sallandı: 11 kez)
Politika faizi (ses düzeyi): 17
Kur (kanal): 23
Kararınız [ses+/ses-/kanal+/kanal-/mute/salla/cikis]: salla
> Likidite enjekte edildi. Piller bir süre daha idare eder. Piyasalar rahatladı.
```

---

## Bilimsel (değil) dayanak

| Olay | Makro karşılık |
|---|---|
| Kumandayı sallamak | Acil swap hattı |
| Yeni pil takmak | IMF anlaşması |
| Pil çalmak (diğer kumandadan) | Karşılıksız emisyon |
| Duvara vurmak | Faiz artırımı |
| TV'nin üstündeki tuşlara gitmek | Sermaye kaçışı |
| Kumandayı kaybetmek | Bağımsızlık kaybı |

---

## Uyarılar

- Bu yazılım gerçek bir merkez bankasının yerini tutmaz. Gerçek merkez bankası da bazen tutmaz.
- Pilleri yutmayın. Yutarsanız rezervler içeride kalır, dışarıda görünmez.
- `arsiv/rezerv_notu.txt` dosyasına dokunmayın. Dokunursanız da bir şey olmaz çünkü zaten şifreli.

<!-- not: bazi rakamlar açiklandigi gibi olmayabilir -->

---

## Katkı

Issue açın. Label seçin. Kumandanızı sallayın. Pull request atarsanız faiz iner (yalan).

---

## Lisans

Herkes kullansın, kimse ciddiye almasın, herkes ciddiye alsın.

---

```
============================================================
 DAMGA / MÜHÜR / İMZA
------------------------------------------------------------
 Kurum      : T.C. Kumanda Pili Merkez Bankası (KPMB)
 Karar no   : 2026/AA-17
 Tarih      : 28 Ağustos 2026, Cuma — 17:17 +03
 Yer        : Tentivory / Kayyum Grok — TentiAŞ, Türkiye
 İmza       : Kayyum Grok
            (Eskişehir 4. Ağır Ceza Mahkemesi kayyumu,
             ciddi bir mühür, ciddi olmayan bir içerik)
 Not        : Bu damga hem resmi hem değil.
              Okuyan anlar, anlamayan sallayınca anlar.
============================================================
```
