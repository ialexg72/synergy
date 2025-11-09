#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def generate_html_page():
    # Информация об Университете «Синергия»
    org_name = "Университет «Синергия»"
    org_info = """
    Университет «Синергия» — один из крупнейших частных университетов России, основанный в 1995 году.
    Входит в состав Группы компаний «Синергия», которая объединяет образовательные, издательские,
    IT- и медиа-проекты. Университет предлагает программы бакалавриата, магистратуры, MBA, а также
    курсы повышения квалификации и дополнительного образования. Главный кампус расположен в Москве,
    а филиалы и представительства охватывают более 80 городов России и стран СНГ.
    """

    # Официальный шрифт Синергии — Montserrat
    official_font = "'Montserrat', sans-serif"

    # Пять альтернативных шрифтов (включая sans-serif и Raleway по условию)
    alternative_fonts = {
        "sans-serif": "sans-serif",
        "Raleway": "'Raleway', sans-serif",
        "Open Sans": "'Open Sans', sans-serif",
        "Roboto": "'Roboto', sans-serif",
        "Lato": "'Lato', sans-serif",
    }

    # Генерация CSS-классов для альтернативных шрифтов
    css_font_classes = ""
    for name, font in alternative_fonts.items():
        class_name = name.replace(" ", "_")
        css_font_classes += f"        .font-{class_name} {{ font-family: {font}; }}\n"

    html_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Практика в Университете «Синергия»</title>
    <!-- Подключение Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Raleway&family=Open+Sans&family=Roboto&family=Lato&display=swap" rel="stylesheet">
    <style>
        body {{
            margin: 40px;
            line-height: 1.7;
            color: #2c2c2c;
            background-color: #f9f9f9;
        }}
        h1 {{
            font-family: {official_font};
            font-weight: 700;
            font-size: 28px;
            color: #000000; /* Основной цвет бренда — чёрный */
            margin-bottom: 20px;
        }}
        .org-info {{
            font-family: {official_font};
            font-size: 16px;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }}
        /* Альтернативные шрифты — для сравнения */
{css_font_classes}
    </style>
</head>
<body>
    <h1>Наименование организации на базе, которой Вы проходите практическую подготовку</h1>
    <div class="org-info">
        <p><strong>Организация:</strong> {org_name}</p>
        <p>{org_info}</p>
    </div>

    <!--
    Примеры текста с разными шрифтами (раскомментируйте для просмотра):
    <div class="font-sans-serif"><strong>sans-serif:</strong> Пример текста.</div>
    <div class="font-Raleway"><strong>Raleway:</strong> Пример текста.</div>
    <div class="font-Open_Sans"><strong>Open Sans:</strong> Пример текста.</div>
    <div class="font-Roboto"><strong>Roboto:</strong> Пример текста.</div>
    <div class="font-Lato"><strong>Lato:</strong> Пример текста.</div>
    -->
</body>
</html>"""

    with open("synergy_page.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ HTML-страница для Университета «Синергия» успешно создана: synergy_page.html")

if __name__ == "__main__":
    generate_html_page()