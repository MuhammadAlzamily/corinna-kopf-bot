## Corinna Kopf Images bot

** How to install and use the tool **

1. first off go to [reddit]() and create a new app and get ONLY an app ID and a secret key and replace the placeholders in the script
2. CLone the repo using `git clone <repo name>`
3. navigate into the directory `cd nsfw`
4. Then run `python3 image_scraper.py` if you're on linux or `python image_scraper.py` if you're on windows

*** Important notes ***

- The bot can be run 24/7 using AWS / digital Ocean / Raspberry Pi to get the latest pictures of her 

 - The bot will not repeat the images - unless the subreddit posted the same pics ofc - as i'm using the post's ID as the filename so it won't repeat the pics 

*Any ways to improve the project are highly appreciated*

*Feel free to use or modify the script the way you please*