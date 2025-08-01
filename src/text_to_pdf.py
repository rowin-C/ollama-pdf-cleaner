from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth

def save_text_as_pdf(texts: list[str] | str, output_path: str):
    if isinstance(texts, str):
        texts = [texts]

    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    margin = 50
    line_height = 14
    max_width = width - 2 * margin
    max_lines = int((height - 2 * margin) / line_height)

    for page_text in texts:
        y = height - margin
        lines = page_text.split('\n')
        line_count = 0

        for line in lines:
            words = line.strip().split()
            current_line = ""
            for word in words:
                test_line = current_line + " " + word if current_line else word
                if stringWidth(test_line, "Helvetica", 12) < max_width:
                    current_line = test_line
                else:
                    c.drawString(margin, y, current_line)
                    y -= line_height
                    line_count += 1
                    current_line = word

                    if line_count >= max_lines:
                        c.showPage()
                        y = height - margin
                        line_count = 0
            if current_line:
                c.drawString(margin, y, current_line)
                y -= line_height
                line_count += 1

                if line_count >= max_lines:
                    c.showPage()
                    y = height - margin
                    line_count = 0

        c.showPage()

    c.save()
    print(f"✅ PDF saved to {output_path}")
