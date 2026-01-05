# graphs/latex_renderer.py
def render_bar_chart(values, x_label, y_label):
    coords = "\n".join(
        f"({i+1},{v})" for i, v in enumerate(values)
    )

    latex = rf"""
\begin{{tikzpicture}}
\begin{{axis}}[
    ybar,
    xlabel={{{x_label}}},
    ylabel={{{y_label}}},
    symbolic x coords={{{",".join(str(i+1) for i in range(len(values)))}}},
    xtick=data
]
\addplot coordinates {{
{coords}
}};
\end{{axis}}
\end{{tikzpicture}}
"""
    return latex.strip()
