from math_physics.pix2text_engine import image_to_latex_blocks

def parse_formula(image_path: str):
    blocks = image_to_latex_blocks(image_path)

    latex_lines = []

    # 1. Add question text
    for line in blocks["text_blocks"]:
        latex_lines.append(f"\\text{{{line}}}\\\\")
    
    # 2. Add equations
    for eq in blocks["math_blocks"]:
        latex_lines.append("\\[")
        latex_lines.append(eq)
        latex_lines.append("\\]")

    final_latex = "\n".join(latex_lines)

    return {
        "latex": final_latex,
        "type": "math_question",
        "confidence": "medium"
    }
