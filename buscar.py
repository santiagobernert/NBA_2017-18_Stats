import jyserver.Flask as jsf
from bigdata import jugadores as jg, df


equipos = {
    'atlanta hawks': 'ATL',
    'boston celtics': 'BOS',
    'brooklyn nets': 'BRK',
    'charlotte hornets': 'CHO',
    'chicago bulls': 'CHI',
    'cleveland cavaliers': 'CLE',
    'dallas mavericks': 'DAL',
    'denver nuggets': 'DEN',
    'detroit pistons': 'DET',
    'golden state warriors': 'GSW',
    'houston rockets': 'HOU',
    'indiana pacers': 'IND',
    'los angeles clippers': 'LAC',
    'los angeles lakers': 'LAL',
    'memphis grizzlies': 'MEM',
    'miami heat': 'MIA',
    'milwaukee bucks': 'MIL',
    'minnesota timberwolves': 'MIN',
    'new orleans pelicans': 'NOP',
    'new york knicks': 'NYK',
    'oklahoma thunder': 'OKC',
    'orlando magic': 'ORL',
    'philadelphia 76ers': 'PHI',
    'phoenix suns': 'PHO',
    'portland trail blazers': 'POR',
    'sacramento kings': 'SAC',
    'san antonio spurs': 'SAS',
    'toronto raptors': 'TOR',
    'utah jazz': 'UTH',
    'washington wizards': 'WAS',
}


pos = {
    'Todas':'PG SG SF PF C',
    'Base': 'PG',
    'Escolta': 'SG',
    'Alero': 'SF',
    'Ala-Pivot': 'PF', 
    'Pivot': 'C'
}

