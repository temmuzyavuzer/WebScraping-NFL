# WEB SCRAPING AND SOCIAL MEDIA SCRAPING
## Final Project Description and Analysis
#### Scraping NFL Player Stats
###### *Description of the Topic and the Web Page*

The National Football League (NFL) is a professional American football league that consists of 32 teams. The NFL is one of the major North American professional sports leagues and the highest professional level of American football in the world. Each NFL season begins with a three-week preseason in August, followed by the eighteen-week regular season, which runs from early September to early January. Each team plays seventeen games and has one bye week. Following the conclusion of the regular season, seven teams from each conference (four division winners and three wild card teams) advance to the playoffs, a single-elimination tournament that culminates in the Super Bowl.

The goal of the project is to scrape results for NFL player stats, especially for the players combined seasons, age 26 or younger, who were drafted between 1936 and 2021, sorted by descending Passing TD. Because of the points scored by touchdowns could lead to getting 6 to 8 points which are most crucial for a team to win the game. 

The data to be scraped includes basic information about the player's career stats, such as 
Games Played (GS), Approximate Value (AV), Team record in-game started by this QB (QBrec), Percentage of Successful Passes (Cmp%), Yards gained by passing(Yds),
Yards gained by pass attempts(Y/A), Passing Touchdowns (TD), Interceptions Thrown (Int), Fantasy Points (FantPt).

[The starting page](https://stathead.com/tiny/tTuxM) to be used in this project is linked then the codes will go to each player profile to scrape their data such as [this web site](https://www.pro-football-reference.com/players/M/MariDa00.htm).

###### Short description of your scraper mechanics 
- BeautifulSoup:
Code starts from the [main page]('https://stathead.com/tiny/tTuxM')
Takes all the players urls in main page and store it into an array which called as “links”
Scrape players’ career information from the html text of the players urls
Print it on the console as a dictionary
Store this information to the ‘player.csv’ file

- Selenium:
Code starts from the main page
Then navigate to each player in the first list
After that, it goes to each player's profile
Scrape their career stats
Print it on the console as a dictionary

- Scrapy:
Code starts from the main page
Takes all of the players urls and store it into a text file called info.txt
After that, it goes to each player's profile using those urls
Stores the html files of each player inside of folder called all_data
Scrape their career stats
Print it on the console as a dictionary

***Data analysis and interpretation part of the project is in [the link](Web Scraping - Final Project Description and Analysis.pdf). :trollface: ***


