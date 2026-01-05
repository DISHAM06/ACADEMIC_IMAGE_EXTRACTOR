# graphs/test_bar_pipeline.py
from graphs.graph_detector import is_bar_chart
from graphs.axis_extractor import extract_axis_labels
from graphs.bar_extractor import extract_bars
from graphs.latex_renderer import render_bar_chart

IMAGE = "input/images/bar_chart.jpg"

def run():
    print("\n[INFO] Checking graph type...")
    if not is_bar_chart(IMAGE):
        print("❌ Not a bar chart")
        return

    print("✅ Bar chart detected")

    x_label, y_label = extract_axis_labels(IMAGE)
    values = extract_bars(IMAGE)

    latex = render_bar_chart(values, x_label, y_label)

    print("\n========== LATEX OUTPUT ==========\n")
    print(latex)
    print("\n=================================\n")

if __name__ == "__main__":
    run()
