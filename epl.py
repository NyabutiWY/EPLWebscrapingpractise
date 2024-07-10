import requests
from bs4 import BeautifulSoup
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import json
url = 'https://www.premierleague.com/tables?co=1&se=578&ha=-1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')


data = []
rows = soup.find_all('tr', class_='tableMid')

for row in rows:
    compseason = row['data-compseason']
    position = row['data-position']
    tds = row.find_all('td')
    if len(tds) >= 11:
        matches_played = tds[2].text.strip()
        wins = tds[3].text.strip()
        draws = tds[4].text.strip()
        losses = tds[5].text.strip()
        goals_scored = tds[6].text.strip()
        goals_conceded = tds[7].text.strip()
        goal_difference = tds[8].text.strip()
        points = tds[9].text.strip()
        data.append([
            compseason,
            position,
            matches_played,
            wins,
            draws,
            losses,
            goals_scored,
            goals_conceded,
            goal_difference,
            points
        ])


doc = SimpleDocTemplate("epl_table.pdf", pagesize=landscape(A4))
elements = []


styles = getSampleStyleSheet()
title = Paragraph("Premier League Table", styles['Title'])
elements.append(title)
elements.append(Spacer(1, 12))

table_data = [['Compseason', 'Position', 'Played', 'Wins', 'Draws',
               'Losses', 'Goals\nScored', 'Goals\nConceded', 'Goal\nDifference', 'Points']]
print(data)
table_data.extend(data)
print(table_data, sep="\n")

col_widths = [80, 50, 50, 50, 50, 50, 60, 60, 60, 50]

table = Table(table_data, colWidths=col_widths)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))

elements.append(table)


doc.build(elements)

filtered_data = [{
    'compseason': item[0],
    'position': item[1],
    'matches_played': item[2],
    'wins': item[3],
    'draws': item[4],
    'losses': item[5],
    'goals_scored': item[6],
    'goals_conceded': item[7],
    'goal_difference': item[8],
    'points': item[9]
} for item in data]

with open('epl.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=4)
