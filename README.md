# voyager

## What is Voyager
  Voyager is a simple path finding game in an unexplored world. The goal is to
  reach the destination cell by spending least amount of enery.

## Rules/How to play
  - An agent can move in any four direction: North, East, South or West.
  - With every move there is an amount of energy that needs to be spent.
  - Surrounding cells are revealed when agent moves to a cell.
  - The type of the cell determines how much energy is needed to move to that cell.
  - There are no obstacles, that is, an agent can move to any cell. Although the
    amount of enery needed to move to a cell might make it prohibitively expensive.
  - Therefore, the destination is always reachable.

## Programmatic Interface
  - HTTP `GET` and `POST` calls to the server can be used to play this game.
  - A bot in any language can be used to make the calls and play the game.

## TODO
- [ ] Map Generation
- [ ] Better Graphics:
  - [ ] Cell
  - [ ] Agent(s)
  - [ ] Layout
- [ ] Multiple Agents
- [ ] Persistence
  - [ ] Score
  - [ ] Moves
- [ ] Playback
- [ ] AI
