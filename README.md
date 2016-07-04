# /r/DailyProgrammer scraper
Script that scrapes the [/r/dailyprogrammer](https://www.reddit.com/r/dailyprogrammer) subreddit and stores the challenges locally (as .md files).

```sh
git clone https://github.com/mteeney01/daily_programmer_scraper.git
cd ./daily_programmer_scraper
pip install -r requirements.txt
python ./challenge-scraper.py
```

This will create a `challenges` directory at the current location, along with subdirectories for the `[Easy]`,`[Intermediate]`, and `[Hard]` challenges.
