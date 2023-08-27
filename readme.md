# assignment
This repo startcode for computer science students of Stanislascollege Westplantsoen havo 4 and vwo 4.
The description of the assignment can be found at
[https://github.com/SCW-IN/hv4-game-startcode/blob/main/game.md](https://github.com/SCW-IN/hv4-game-startcode/blob/main/game.md)

# pygame with pygbag in replit - proof of concept 
This repo runs python with pygame in the browser, using pybag to compile python to webassembly. 
It uses replit as an IDE for editting, compiling and hosting.

# How to use
1. Import repo in replit [![Run on Repl.it]](https://replit.com/badge/github/vangeest/pygame-pygbag-replit-poc)](https://replit.com/new/github/vangeest/pygame-pygbag-replit-poc)
2. Edit source code of game in mygame/main.
3. Push run button in replit to rebuild game.
4. Start mygame by using these links to play the game, with and without debug info
    https://replit.com/@YOUR_LOGIN/YOUR_REPO/mygame/build/web/index.html#debug <br>
    https://replit.com/@YOUR_LOGIN/YOUR_REPO/mygame/build/web/index.html <br>

# Documentation
- more info on pygbag:
  https://pypi.org/project/pygbag/

# How this repo was constructed
- Create repl and choose language python
  (Pygame repl adds pygame package and uses vnc to stream grahpics. 
  The pygame package will be automatically added by replit.
  vnc we do not need as our code will run client side because we use pygbag)
- Save the result in a github repo
  (sometimes replit can't create the repo, don't know why, this time I was lucky)
- Add test game from pygbag (https://github.com/pygame-web/pygbag/tree/main/test) in folder mygame 
- Execute `pip3 install pygbag` in replit shell
- Execute `python -m pygbag --build mygame` in replit shell
- Add index.html with links to where the web-version of the game is build by pygbag
- Execute `python -m http.server` in replit shell
- Oeps, the index.html is only shown briefly after Run button had been hit->
  comment out [interpreter] section in .replit file
  change [run] to "python -m http.server"
- automatically rebuild mygame by changing [run] command to "python -mpygbag --build mygame && python -m http.server"
- several non essential modifcations

# Github
- This repl is pushed to https://github.com/vangeest/pygame-pygbag-replit-poc
- Imported the repl from github into replit webinterface and with https://replit.com/github/vangeest/pygame-pygbag-replit-poc <br>
  both didn't go well, because 1) mostly it takes forever, 2) the .replit file (and repl configuration?) is changed during import
- Imported the repl from github into replit with https://replit.com/new/github/vangeest/pygame-pygbag-replit-poc (notice "/new") <br>
  importing is most of the time succesfull, but it changes over 2000! files (packages probably)
- Committed and pushed all changes (over 2000 files for packages replit added for a reason I don't understand)
- Tried removing venv map from the repo, hoping the poetry packages installer that replit uses would take care of rebuilding venv, but it didn't. Reverted this change.

Status: import is often succesfully completed after 1 minute, other times it takes forever.
Work aroud: in classrooms, let students not use github. Let them fork a repl in replit, not a repo from github. For now I consider this acceptable.
