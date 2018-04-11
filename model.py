#model.py
import csv
import operator
BB_FILE_NAME = 'umbball.csv'
FB_FILE_NAME = 'umfball.csv'

bb_seasons = []
fb_seasons = []

def init_bball(csv_file_name):
    global bb_seasons
    with open(csv_file_name) as f:
        reader = csv.reader(f)
        next(reader) # throw away headers
        next(reader)
        global bb_seasons
        bb_seasons = [] # reset, start clean
        for r in reader:
            r[3] = int(r[3])
            r[4] = int(r[4])
            r[5] = float(r[5])
            bb_seasons.append(r)

def get_row_col(row, colnum):
    return row[colnum]

def get_bball_seasons(sortby='year', sortorder='desc'):
    if len(bb_seasons) == 0:
        init_bball(BB_FILE_NAME)

    if sortby == 'year':
        sortcol = 1
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 5
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    # sorted_list = sorted(bb_seasons, key=get_row_col(sortcol) lambda x: x[sortcol], reverse=rev)
    sorted_list = sorted(bb_seasons, key=operator.itemgetter(sortcol), reverse=rev)
    return sorted_list
