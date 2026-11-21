# Space Invaders

Pygame shooter, checkpoint 1 version: the player ship moves and fires, enemy waves fall, enemies that reach the bottom cost a life.

```
space-invaders/
├── main.py           # game loop (window, waves, collisions, lives)
├── settings.py       # WIDTH, HEIGHT
├── assets.py         # image loading relative to this folder
├── GameClass.py      # Game: lives, level, HUD, game over, quit event
├── ShipClass.py      # Ship: base class (position, health, draw)
├── PlayerClass.py    # Player(Ship): movement, bullets, cooldowns, hit
├── EnemyClass.py     # Enemy(Ship): colors, move, create waves, speed
├── BulletClass.py    # Bullet: move, draw, mask collision
├── DrawingClass.py   # Drawing: background, ships, HUD per frame
└── img/              # background, player, bullet, enemy and shot PNGs
```

## Run

```bash
../../.venv/bin/python -m pip install -r ../../requirements.txt
../../.venv/bin/python main.py
```

Keys: arrows or `WASD` move, `SPACE` fire, close the window to quit.
