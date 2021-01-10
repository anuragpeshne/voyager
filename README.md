# voyager

## What is Voyager
  Voyager is a simple path finding game in an unexplored world. The goal is to
  reach the destination cell by spending least amount of energy.

## Rules/How to play
  - An agent can move in any of the four direction: North, East, South or West.
  - Surrounding cells are revealed when agent moves to a cell.
  - With every move there is an amount of energy associated that needs to be spent.
  - The type of the cell determines how much energy is needed to move to that cell.
  - There are no obstacles, that is, an agent can move to any cell. Although the
    amount of enery needed to move to a cell might make it prohibitively expensive.
  - Therefore, the destination is always reachable.

## Programmatic Interface
  - HTTP `GET` and `POST` calls to the server can be used to play this game.
  - A bot in any language can be used to make the calls and play the game.

## TODO
- [ ] Graphics:
  - [ ] Cell
  - [ ] Agent(s)
  - [ ] Layout
- [ ] Game Design
  - [ ] Map Generation
  - [ ] Types of cells
  - [ ] Energy associated with cells
  - [ ] Multiple Agents
- [ ] Persistence
  - [ ] Score
  - [ ] Moves
  - [ ] Playback
- [ ] Engineering/Operations
  - [ ] Docker Image for the server
  - [ ] DB: SQLite?
- [ ] AI
  - [ ] Astar
  - [ ] RL
