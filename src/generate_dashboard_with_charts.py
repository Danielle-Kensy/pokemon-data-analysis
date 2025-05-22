from jinja2 import Environment, FileSystemLoader
import os

def generate_dashboard_with_charts(graphics_folder, output_html="pokemon_dashboard.html"):
    # pega os pngs
    files = sorted([f for f in os.listdir(graphics_folder) if f.endswith(".png")])
    charts = []

    for file in files:
        title = file.replace("_", " ").replace(".png", "").capitalize()
        relative_path = os.path.join(graphics_folder, file)
        charts.append((title, relative_path))

    # load do jinja
    env = Environment(loader=FileSystemLoader("dashboard"))
    template = env.get_template("template.html")

    # renderiza e salva o dashboard
    rendered_html = template.render(charts=charts)
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(rendered_html)
    
    print(f"✅ Dashboard gerado em: {output_html}")