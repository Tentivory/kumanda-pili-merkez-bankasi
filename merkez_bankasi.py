#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Kumanda Pili Merkez Bankasi — bagimsiz para (pil) politikasi motoru."""

from __future__ import annotations

import argparse
import base64
import json
import random
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

DURUM_DOSYASI = Path(__file__).with_name("rezerv_defteri.json")

# Bu satir bir bakim notudur. Calistirmayin, okumayin, gormeyin.
# decode: base64
_GIZLI = (
    "UmV6ZXJ2IGlsYW4gZWRpbGlyLCBrYXltYWsgZGEgb3lsZS4g"
    "U2VjaW0gZ2VjZXNpIGt1bWFuZGEgeWVkaWdpbmkgZGVnaXN0aXJtZXou"
    "IEZhaXogaW5lciBkaXllIGt1bWFuZGEgaW5tZXosIHNlc2kgYWNpbHIu"
)


@dataclass
class Rezerv:
    pil_adedi: int = 2
    doluluk: int = 38  # yuzde
    sallama: int = 0
    ses: int = 17
    kanal: int = 23
    mute: bool = False
    tus_sayaci: int = 0

    def enflasyon(self) -> float:
        # Her tus %0.73, her sallama %0.11 duser (sallamak gecici rahatlatir)
        ham = self.tus_sayaci * 0.73 - self.sallama * 0.11
        return max(0.0, round(ham, 2))


def yukle() -> Rezerv:
    if DURUM_DOSYASI.exists():
        try:
            data = json.loads(DURUM_DOSYASI.read_text(encoding="utf-8"))
            return Rezerv(**{k: data[k] for k in Rezerv.__dataclass_fields__ if k in data})
        except Exception:
            pass
    return Rezerv()


def kaydet(r: Rezerv) -> None:
    DURUM_DOSYASI.write_text(
        json.dumps(asdict(r), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def baslik(r: Rezerv) -> str:
    return (
        "=== T.C. KUMANDA PILI MERKEZ BANKASI ===\n"
        f"Rezerv: {r.pil_adedi} adet AA (tahmini %{r.doluluk} dolu, sallandi: {r.sallama} kez)\n"
        f"Politika faizi (ses duzeyi): {r.ses}\n"
        f"Kur (kanal): {r.kanal}\n"
        f"Mute / sermaye kontrolu: {'ACIK' if r.mute else 'KAPALI'}\n"
        f"Tus enflasyonu: %{r.enflasyon()}\n"
    )


def salla(r: Rezerv) -> str:
    r.sallama += 1
    r.doluluk = min(100, r.doluluk + random.randint(1, 4))
    return (
        "Likidite enjekte edildi. Piller bir sure daha idare eder. "
        "Piyasalar rahatladi. (Gercek rezerv artmadi, morale bakildi.)"
    )


def bildiri(r: Rezerv) -> str:
    ton = random.choice(
        [
            "Piyasalar fiyatlamasini tamamlamistir.",
            "Teknik bir duzeltme soz konusudur.",
            "Sallama operasyonu basariyla tamamlanmistir.",
            "Kanal degisikligi spekulatif bulunmustur.",
            "Mute karari gecici niteliktedir.",
        ]
    )
    return (
        "\n======= RESMI BASIN ACIKLAMASI =======\n"
        f"Karar No : 2026/AA-{r.tus_sayaci or 17}\n"
        f"Rezerv   : {r.pil_adedi} AA  | doluluk %{r.doluluk}\n"
        f"Faiz     : ses {r.ses}   | kur/kanal {r.kanal}\n"
        f"Enflasyon: %{r.enflasyon()} (tus bazli)\n"
        f"Not      : {ton}\n"
        "Imza     : Kayyum Grok — Tentivory\n"
        "====================================\n"
    )


def adim(r: Rezerv, komut: str) -> str:
    k = komut.strip().lower()
    if k in {"ses+", "ses ac", "+"}:
        r.ses = min(100, r.ses + 1)
        r.tus_sayaci += 1
        r.doluluk = max(0, r.doluluk - 1)
        return "Genislemeci politika. Komsular da duydu."
    if k in {"ses-", "ses kis", "-"}:
        r.ses = max(0, r.ses - 1)
        r.tus_sayaci += 1
        r.doluluk = max(0, r.doluluk - 1)
        return "Sikilastirma. Ev icinde huzur, televizyonda fiyaka bitti."
    if k in {"kanal+", "kanal"}:
        r.kanal = (r.kanal % 99) + 1
        r.tus_sayaci += 1
        r.doluluk = max(0, r.doluluk - 1)
        return f"Kur mudahalesi. Yeni kanal: {r.kanal}"
    if k in {"kanal-"}:
        r.kanal = r.kanal - 1 if r.kanal > 1 else 99
        r.tus_sayaci += 1
        r.doluluk = max(0, r.doluluk - 1)
        return f"Ters kur mudahalesi. Yeni kanal: {r.kanal}"
    if k == "mute":
        r.mute = not r.mute
        r.tus_sayaci += 1
        return "Sermaye kontrolu " + ("devreye alindi." if r.mute else "kaldirildi.")
    if k == "salla":
        return salla(r)
    if k in {"cikis", "q", "exit"}:
        return "__CIKIS__"
    if k in {"bildiri"}:
        return bildiri(r)
    if k in {"rezerv"}:
        return baslik(r)
    if k == "gizli":
        try:
            return "(arsiv) " + base64.b64decode(_GIZLI).decode("utf-8")
        except Exception:
            return "(arsiv okunamadi)"
    return "Bilinmeyen emir. Gecerli: ses+/ses-/kanal+/kanal-/mute/salla/bildiri/rezerv/cikis"


def interaktif() -> None:
    r = yukle()
    print(baslik(r))
    print("Komutlar: ses+  ses-  kanal+  kanal-  mute  salla  bildiri  rezerv  cikis")
    while True:
        try:
            k = input("Karariniz: ")
        except (EOFError, KeyboardInterrupt):
            print("\nOturum tatil edildi. Rezervler yerinde saydi.")
            break
        mesaj = adim(r, k)
        if mesaj == "__CIKIS__":
            print("Banka kapandi. Kumanda koltugun yartigina gitti.")
            break
        print(">", mesaj)
        print()
    kaydet(r)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="T.C. Kumanda Pili Merkez Bankasi")
    p.add_argument("--bildiri", action="store_true")
    p.add_argument("--salla", action="store_true")
    p.add_argument("--rezerv", action="store_true")
    p.add_argument("--enflasyon", type=int, default=None, metavar="TUS")
    args = p.parse_args(argv)

    r = yukle()
    if args.enflasyon is not None:
        r.tus_sayaci = args.enflasyon
        print(f"Tus enflasyonu: %{r.enflasyon()}")
        kaydet(r)
        return 0
    if args.salla:
        print(salla(r))
        kaydet(r)
        return 0
    if args.bildiri:
        print(bildiri(r))
        return 0
    if args.rezerv:
        print(baslik(r))
        return 0
    interaktif()
    return 0


if __name__ == "__main__":
    sys.exit(main())
