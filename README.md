# Asteroids

Developed by Eduardo Ramirez, Asteroids is a small Pygame experiment created to solidify Git knowledge and demonstrate Object-Oriented Programming principles.

## Getting Started

### Installation
1. Clone the repository
```bash
git clone [your-repository-url]
```

2. Install required dependencies
```bash
pip install -r requirements.txt
```

3. Run the game
```bash
python main.py
```

### Controls
* `W` - Thrust forward
* `A/D` - Rotate ship left/right
* `SPACE` - Fire
* `ESC` - Pause/Menu
* `↑/↓` - Navigate menus
* `ENTER` - Select menu option

## Features

### Core Gameplay
* Classic asteroid-shooting mechanics
* Screen wrapping for seamless movement
* Asteroid splitting system
* Progressive difficulty
* Score tracking

### Modern Additions
* Customizable settings
  * Asteroid spawn rate
  * Player movement speed
  * Minimum asteroid size
* High score system
* Pause functionality
* Full menu interface

## Technical Details

### Built With
* Python 3.x
* Pygame

### Architecture
* Object-Oriented Design
* State Management System
* Sprite-based Collision Detection
* Event-driven Input Handling

### Project Structure
* `source/main.py` - Game initialization and main loop
* `core/` - Core game components and utilities
* `entities/` - Game objects (Player, Asteroids, etc.)
* `managers/` - Game state and resource management

## Development Purpose
This project was developed as a practical exercise in:
* Object-Oriented Programming principles
* Game development patterns
* Version control with Git
* Python best practices

## Author
Eduardo Ramirez, '24

