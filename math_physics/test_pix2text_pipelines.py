from math_physics.formulae import parse_formula

result = parse_formula("input/images/questionlist.jpg")
print("\n=== FINAL LATEX ===\n")
print(result["latex"])
