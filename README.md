# Instagram Scraper
#### An easy-to-use instagram public details (Followers, following, post count) scraper.
<hr>

# Installation
> `git clone https://github.com/vivekshah1801/Instagram-Fried-Potato`


# Usage
This scraper runs in two modes.
- Batch Mode (Takes input from file and scrapes details in batch, optionally saves output to csv file)
- Interactive Mode (Takes input from console, scrapes one profile only, useful for quick test)

### Batch Mode Usage
> `python3 main.py -f path/to/file [-q] [-o path/to/output]`
- -f : Path to input file with profile ids to scrape.
- -q : Quite flag, surpresses any error. [Optional]
- -o : Output file path where csv of results will be saved, if not provided outputs to console. [Optional]

### Interactive Mode Usage
> `python3 main-interactive.py`

# Screenshots

- Batch Mode
![batch mode execution](https://user-images.githubusercontent.com/34334421/97490586-1182db80-1987-11eb-86e4-7424c328b369.png)

- Interactive Mode
![interactive mode execution](https://user-images.githubusercontent.com/34334421/97490646-23647e80-1987-11eb-93a4-325d439184a1.png)

<hr>
#### [vivekshah.tech](https://vivekshah.tech)