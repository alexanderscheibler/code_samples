"""
Constant values for the app.
"""

PRICE_TABLE = {
    3: {
        "weekday": {
            "regular": 110,
            "rewards": 80
        },
        "weekend": {
            "regular": 90,
            "rewards": 80
        },
        "establishment": ["Economy"]
    },
    4: {
        "weekday": {
            "regular": 160,
            "rewards": 110
        },
        "weekend": {
            "regular": 60,
            "rewards": 50
        },
        "establishment": ["Medium"]
    },
    5: {
        "weekday": {
            "regular": 220,
            "rewards": 100
        },
        "weekend": {
            "regular": 150,
            "rewards": 40
        },
        "establishment": ["Luxury"]
    }
}
