

# replit configurationn for pygbag 
more info on pygbag:
https://pypi.org/project/pygbag/

# Steps to recreate:
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
- it works, basically, todo:
- pygbag compile automatically (instead of via shell command)
- adjust name op repl an repo (typo pybag must be bygbag)