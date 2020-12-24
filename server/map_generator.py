def generate(map_name):
    name, size = map_name.split('_')
    if name == 'nile':
        return __generate_nile(size)
    elif name == 'himalaya':
        return __generate_himalaya(size)
    else:
        return __generate_default(size)

def __generate_nile(size):
    map_ = [
        [1,   1,   1,   500, 1, 1, 1, 1],
        [1,   1,   1,   500, 1, 1, 1, 1],
        [1,   1,   500, 500, 1, 1, 1, 1],
        [1,   500, 1,   500, 1, 1, 1, 1],
        [500, 1,   1,   500, 1, 1, 1, 1],
        [1,   1,   500,   1, 1, 1, 1, 1],
        [1,   500,   1,   1, 1, 1, 1, 1],
        [500,   1,   1,   1, 1, 1, 1, 1]
    ]

    return {
        'start': [len(map_) - 2, 0],
        'dest': [0, len(map_[0]) - 1],
        'map': map_
    }

def __generate_himalaya(size):
    map_ = [
        [  1,   1,   1, 1,  1,   1,   1,  19],
        [  1,   1,   1, 1,  1,   1,  19, 299],
        [299,   1,   1, 1,  1,  19, 299, 499],
        [499, 299,   1, 1, 19, 299, 499, 899],
        [999, 499, 299, 1,  1,  19, 299, 499],
        [499, 299,   1, 1,  1,   1,  19, 299],
        [299,   1,   1, 1,  1,   1,   1,  19]
    ]

    return {
        'start': [len(map_) - 1, 0],
        'dest': [0, len(map_[0]) - 2],
        'map': map_
    }
