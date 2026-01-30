# COLOR REPLACER

extremely simple python program meant to quickly and easily translate config files from one color scheme to another, tho it can theoretically also be used to perform a lot of text replacements at once

## USAGE

clone the repo, cd into it, then do
```
main.py /path/to/color/file /path/to/json/file
```
The script will print its result to stdout, so to immediately apply it to the file do
```
main.py /path/to/color/file /path/to/json/file > /path/to/color/file
```

you can test this out by taking a file using the catppuccin-macchiato color scheme and running it in the script together with ```macchiato-to-mocha.json```
