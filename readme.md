

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
- add test game from pygbag (https://github.com/pygame-web/pygbag/tree/main/test) in folder mygame 

# - add links in index.html to mygame
# - in replit shell execute command pip3 install pygbag
#   when asked, select python39Packages.pip as the nix package to install
#   running into error: 
#    /nix/store/95kl4499yaa91j0ja7vwzf5l7r3ly4b2-python3.9-pip-22.2.2
#    Fatal Python error: init_sys_streams: can't initialize sys standard streams
#    Python runtime state: core initialized
#    Traceback (most recent call last):
#    File "/nix/store/hd4cc9rh83j291r5539hkf6qd8lgiikb-python3-3.10.8/lib/python3.10/io.py", line 54, in <module>
#   cannot fix this, however in a python repl I did succeed to run pygbag
#   so appearenly copying the .replit en .nix doens't do it all 
#   (it may habe to do with replit automatic package loader)
#   so I'm going to give it another go by starting with the python repl
#   and add the server part with python -m http.server
