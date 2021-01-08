# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, request, url_for
import json
import map_generator
import uuid

app = Flask(__name__, static_url_path='/static')
state = {}

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/maps", methods = ['GET'])
def get_maps():
    maps = ['nile_s', 'himalaya_s']
    return json.dumps(maps)

@app.route("/game", methods = ['POST'])
def game():
    player_data = request.form
    print(player_data)
    map_name = player_data['map']
    player_name = player_data['name']

    random_uuid = uuid.uuid4()
    map_data = map_generator.generate(map_name)
    state[random_uuid] = {
        'map_data': map_data,
        'cur_pos': map_data['start'],
        'energy_spent': 0,
        'pname': player_name,
        'explored_cell': {}
    }

    map_ = map_data['map']
    return render_template('game.html',
                           map_dim=[len(map_), len(map_[0])],
                           start=map_data['start'],
                           dest=map_data['dest'],
                           player_name=player_name,
                           uuid=random_uuid)

@app.route("/move", methods = ['POST'])
def move():
    print("in move", request.json)
    move_data = request.json
    key_ = move_data['key']
    to_cell = move_data['to']

    key_uuid = uuid.UUID(key_)
    if key_ is None or key_uuid not in state:
        return redirect(url_for('index'))

    current_state = state[key_uuid]
    map_data = current_state['map_data']
    map_ = map_data['map']
    map_dim = [len(map_), len(map_[0])]
    neighbours = __get_neighbours(to_cell, map_dim)
    explored_neighbours = [[row, col] for [row, col] in neighbours
                           if (row, col) in current_state['explored_cell']]

    if __validate_move(to_cell, current_state):
        if not __check_victory(to_cell, current_state):
            current_state['energy_spent'] += map_[to_cell[0]][to_cell[1]]
        current_state['explored_cell'][tuple(to_cell)] = True
        return json.dumps({
            'peek_cells': [[[row, col], map_[row][col]] for [row, col] in neighbours],
            'energy_spent' : current_state['energy_spent']
        })
    else:
        msg = "Cell [%d, %d] not reachable" % (to_cell[0], to_cell[1])
        print (msg)
        return msg, 401

def __get_neighbours(cell, dim):
    possible_neighbours = [[cell[0] + 1, cell[1]],
                           [cell[0], cell[1] + 1],
                           [cell[0] - 1, cell[1]],
                           [cell[0], cell[1] - 1]]
    return [[row, col] for [row, col] in possible_neighbours
            if row >= 0 and row < dim[0] and col >= 0 and col < dim[1]]

def __validate_move(dest_cell, current_state):
    is_first_move = current_state['cur_pos'] == current_state['map_data']['start']
    map_ = current_state['map_data']['map']
    map_dim=[len(map_), len(map_[0])]
    is_dest_cell_explored = dest_cell in __get_neighbours(current_state['cur_pos'],
                                                          map_dim)
    return is_first_move or is_dest_cell_explored

def __check_victory(to_cell, current_state):
    is_to_destination_cell = to_cell == current_state['map_data']['dest']
    if is_to_destination_cell:
        current_state['is_victorious'] = True
    return ('is_victorious' in current_state or
            is_to_destination_cell)

if __name__ == "__main__":
    app.run()
