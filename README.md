# NinJump

## Contributors:
- Hung Nguyen
- Harry Doan
- Hieu Bui

## Assets source

* Shuriken: https://dk-happy.itch.io/shuriken-ninja
* Weapon: https://dk-happy.itch.io/shuriken-ninja
* Explosion: https://limofeus.itch.io/pixel-simulations
* Codebase, tutorial, platform asset: https://www.youtube.com/c/CodingWithRuss
* flappy bird graphic and sound: https://github.com/samuelcust/flappy-bird-assets
* Fireball: https://xyezawr.itch.io/free-pixel-effects-pack-13-fireballs
* Game background: [https://img.freepik.com/free-vector/ninja-character-background-with-flat-design_23-2147870947.jpg?w=2000](https://img.freepik.com/free-vector/ninja-character-background-with-flat-design_23-2147870947.jpg?w=2000)
* Minecraft sound: https://www.youtube.com/watch?v=0T_NR2KY8uI&ab_channel=GamingSoundFX
* Ninja: [https://www.shutterstock.com/image-vector/ninja-character-sprites-games-animation-644829619](https://www.shutterstock.com/image-vector/ninja-character-sprites-games-animation-644829619)

## Inspiration
We are all in awe with the mystical ninja ninjutsu. When the game’s theme came out, we all came up with the idea of demonstrating these techniques to overcome the edgiest mountain and defeat the villains.

## What it does
The idea is simple. The player will join Huhahimaru, the ninja guy on his journey to defeat the mercilessly ferocious devil standing on the top of a mountain. With his jumping and shuriken ninjutsu, honed through his hard training years, his iron heart is unwaved by this deathly journey.

The **control** is simple. Use **LEFT** and **RIGHT** arrow key to dodge the obstacles, and **SPACE** to throw darts. In the final round, the player will need to use **UP** arrow key to jump.

The game has three main rounds, sorted ascendingly by difficulty. In the first round, Huhahimaru will climb up the mountain on static edges and avoid dangerous obstacles such as the devil flappy birds and the burning flame by the devil. In the second round (500 < score < 1000), his ninjutsu will be further challenged by climbing on moving edges while dodging and killing the obstacles. In these rounds, the jumping is automatic.

Finally, on top fo the mountain, Huhahimaru will face the devil. Let the battle begins!!!

## How we built it
Shout out to [Coding With Russ](https://www.youtube.com/c/CodingWithRuss) who provides very helpful tutorials for pygame. We adapt his code and build our own versions of the game.

- Initially, we sat down together to decide on the theme of the game (which is **ON EDGE**) and brainstormed the idea for the game.
- After coming up with a draft idea, we wrote brief gameplay description and detect relevant objects for the game (e.g, player, bird, fireball, weapon, board, boss)
- Then, we find the relevant assets for the game, along with making the classes' blueprint. Each of us worked on a set of closely related classes ton ensure they are interdependent.
- Finally, once the code was finished, we reviewed and merged them together.

## Challenges we ran into
We are all novice when it comes to game programming, thus, building this game was not an easy task for us. We struggled at first to understand the game-dev concept such as sprites and surfaces. We ran into several hidden bugs due to the large scale of the project. Hitbox is arguably the hardest one to fix as it requires image processing knowledge.

## Accomplishments that we're proud of
POWER OF FRIENDSHIP!!! Lol, even though this is not a shonen manga, we are very proud that we have worked together and built this awesome game. Looking forward to future collab.

FIRST GAME!!! Not perfect, but terrific.

FIRST-HAND EXPERIENCE!!! Backpain and long-hour working is no longer a myth to us 🤢

FUN

## What we learned
- Pygame duhhh.
- Game design
- Project management and version control (e.g. advanced git commands)
- Many more…

## What's next for Ninja Jump
Currently, the objects are walking only on vertical and horizontal axis, with the minimum room for physics and maths simulation. We want to update our game with more of them such as simulating accelerating falling or spontaneous and complex movement.

3D and VR are also appealing idea to integrate into our game.

