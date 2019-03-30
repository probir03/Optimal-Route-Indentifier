def get_dummy_valid_grid(name='grid1'):
    '''Return dummy Grid data'''

    return {
        "name": name,
        "nodes": ["a", "b", "c", "d", "e", "f", "g", "h"],
        "edges": [
            {
                "start": "a",
                "end": "c",
                "distance": 3,
                "speed": 1
            },
            {
                "start": "d",
                "end": "b",
                "distance": 3,
                "speed": 1
            },
            {
                "start": "g",
                "end": "h",
                "distance": 5,
                "speed": 1
            },
            {
                "start": "h",
                "end": "f",
                "distance": 2,
                "speed": 3
            },
            {
                "start": "h",
                "end": "d",
                "distance": 3,
                "speed": 5
            },
            {
                "start": "b",
                "end": "f",
                "distance": 3,
                "speed": 1
            },
            {
                "start": "c",
                "end": "d",
                "distance": 2,
                "speed": 1
            },
            {
                "start": "c",
                "end": "e",
                "distance": 3,
                "speed": 10
            },
            {
                "start": "e",
                "end": "d",
                "distance": 3,
                "speed": 10
            }
        ]
    }

def get_dummy_invalid_grid(name='grid2'):
    '''Return dummy Grid data'''

    return {
        "name": name,
        "nodes": ["a", "b", "c", "d", "e", "f", "g", "h"],
        "edges": [
            {
                "start": "d",
                "end": "b",
                "distance": 3,
                "speed": 1
            },
            {
                "start": "g",
                "end": "h",
                "distance": 5,
                "speed": 1
            },
            {
                "start": "h",
                "end": "f",
                "distance": 2,
                "speed": 3
            },
            {
                "start": "h",
                "end": "d",
                "distance": 3,
                "speed": 5
            },
            {
                "start": "b",
                "end": "f",
                "distance": 3,
                "speed": 1
            },
            {
                "start": "c",
                "end": "d",
                "distance": 2,
                "speed": 1
            },
            {
                "start": "c",
                "end": "e",
                "distance": 3,
                "speed": 10
            },
            {
                "start": "e",
                "end": "d",
                "distance": 3,
                "speed": 10
            }
        ]
    }
