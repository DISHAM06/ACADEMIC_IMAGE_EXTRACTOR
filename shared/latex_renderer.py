# shared/latex_renderer.py

import subprocess
import os

def render_chemfig(chemfig_code: str, output_name: str):
    os.makedirs("output", exist_ok=True)

    tex_file = f"output/{output_name}.tex"
    pdf_file = f"output/{output_name}.pdf"

    tex_content = rf"""
\documentclass[border=5pt]{{standalone}}
\usepackage{{chemfig}}
\begin{{document}}
{chemfig_code}
\end{{document}}
"""

    with open(tex_file, "w", encoding="utf-8") as f:
        f.write(tex_content)

    result = subprocess.run(
        [
            "pdflatex",
            "-interaction=nonstopmode",
            "-output-directory=output",
            tex_file
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # 🔴 CRITICAL SAFETY CHECK
    if not os.path.exists(pdf_file):
        print("❌ LaTeX failed to generate PDF")
        print("STDOUT:\n", result.stdout)
        print("STDERR:\n", result.stderr)
        raise RuntimeError("PDF generation failed")

    return pdf_file
