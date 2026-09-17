from pathlib import Path
import re
import svgwrite

WORDS = [
    "Demokratie", "Mitbestimmung", "Wahl", "Stimme", "Freiheit", "Gleichheit",
    "Rechte", "Pflichten", "Verantwortung", "Respekt", "Toleranz", "Beteiligung",
    "Vielfalt", "Gerechtigkeit", "Zusammenhalt", "Kompromiss", "Diskussion",
    "Zuhören", "Entscheiden", "Gemeinschaft", "Mitreden", "Mitgestalten",
    "Kinderrechte", "Grundgesetz", "Menschenwürde", "Solidarität", "Fairness",
    "Teilhabe", "Frieden", "Vertrauen", "Regeln", "Öffentlichkeit", "Gemeinwohl",
    "Streit", "Argumente", "Gespräch", "Mehrheiten", "Minderheiten", "Abstimmung",
    "Offenheit", "Kritik", "Rücksicht", "Gleichberechtigung", "Chancengleichheit",
    "Meinung", "Austausch", "Mitdenken", "Mitentscheiden", "Aushandlung",
    "Interessen", "Zusammenleben", "Anerkennung", "Mitgefühl", "Mitwirkung"
]

BOX_W_MM = 150
BOX_H_MM = 50
MARGIN_MM = 7
OUT_DIR = Path("out_svgs")
OUT_DIR.mkdir(exist_ok=True)

FONT_FAMILY = "Arial"  # alternativ: Helvetica
START_FONT_SIZE = 60

def sanitize_filename(name: str) -> str:
    name = name.strip()
    name = re.sub(r'[\\/:*?"<>|]+', "_", name)
    return name
def estimate_font_size(word: str):
    inner_w = BOX_W_MM - 2 * MARGIN_MM
    inner_h = BOX_H_MM - 2 * MARGIN_MM

    # sehr grobe Näherung, aber praktisch brauchbar
    size = min(
        int(inner_h * 0.75),
        int(inner_w * 1.8 / max(1, len(word)))
    )
    return max(12, size)
def make_svg(word: str):
    font_size = estimate_font_size(word)

    out_path = OUT_DIR / f"{sanitize_filename(word)}.svg"

    dwg = svgwrite.Drawing(
        filename=str(out_path),
        size=(f"{BOX_W_MM}mm", f"{BOX_H_MM}mm"),
        viewBox=f"0 0 {BOX_W_MM} {BOX_H_MM}",
    )

    # Rahmen
    dwg.add(dwg.rect(
        insert=(0, 0),
        size=(BOX_W_MM, BOX_H_MM),
        fill="none",
        stroke="black",
        stroke_width=0.2,
    ))

    # Text zentriert
    dwg.add(dwg.text(
        word,
        insert=(BOX_W_MM / 2, BOX_H_MM / 2),
        text_anchor="middle",
        dominant_baseline="middle",
        font_size=f"{font_size}px",
        font_family=FONT_FAMILY,
        fill="black",
    ))

    dwg.save()
    print(f"Erstellt: {out_path}")
def main():
    for word in WORDS:
        make_svg(word)

if __name__ == "__main__":
    main()