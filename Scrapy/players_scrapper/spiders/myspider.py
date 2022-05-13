import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from scrapy import signals

#Scraping each players career data starting with all player list
#then code goes to each players profile and scrape their career data
# so that it is 100 different page will be scraped with this code
class PlayerSpider(scrapy.Spider):
    name = "multi_spider"
    list_data = {}
    base_column = 10
    def start_requests(self):
        urls = ['https://stathead.com/tiny/tTuxM',]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    rules = (Rule(LinkExtractor(), callback='parse', follow=True), )

#Storing each player's profile urls in a text file
#then it will start to scrape
# via calling main scrape func with reading the text file
    def parse(self, response):
        all_urls = response.css('a::attr(href)').getall()
        i = 0
        j = 0
        for url in all_urls:
            if (url.startswith("https://www.pro-football-reference.com/players") or url.startswith(
                    "http://www.pro-football-reference.com/players")) and (
                    url.endswith(".html") or url.endswith(".htm")):
                with open("info.txt", 'a') as f:
                    f.write(str(url + "\n"))
                    i = i + 1
                    if i == 10:
                        print("Scraping first 10 player because searching 10 different page takes time")
                        break
        file1 = open('info.txt', 'r')
        Lines = file1.readlines()
        for line in Lines:
            j = j + 1
            yield scrapy.Request(url=line, callback=self.parse_summary, meta={'index': j})

#Main scraping function. Storing each html file in all_file folder
#With that way it is easier to scrape the players career data
#this is why I dont have any problem with finding true xpath etcc
#otherwise scrapy having some error for this page.
    def parse_summary(self, response):
        item = response.meta.get('index')
        with open("all_data/info_" + str(item) + ".html", 'a', encoding="UTF-8") as f:
            f.write(str(response.text))
        with open("all_data/info_" + str(item) + ".html", encoding='utf-8') as fp:
            soup1 = BeautifulSoup(fp, 'html.parser')
        with open("all_data/info_" + str(item) + ".html", "wb") as f_output:
            f_output.write(soup1.prettify("utf-8"))
            soup1.prettify()
        with open("all_data/info_" + str(item) + ".html") as fp:
            soup = BeautifulSoup(fp, 'html.parser')

#getting the players name and career stats etc.
#then store it in dictionary
            player_name = str(soup.find("title").text).strip('\n').strip(" ")
            player_name = player_name[0:player_name.find("Stats")]
            stats_pullout = soup.find("div", {"class": "stats_pullout"}).text
            self.list_data[item] = {}
            self.list_data[item]['player_name'] = player_name
            player_career = stats_pullout.split("\n")

#All that loops is for consistency with the other solutions.
#Otherwise there would be some extra spaces in the result.
# But it is also working without those loops
            while ("" in player_career):
                player_career.remove("")
            k = 0
            for every in player_career:
                if player_career[k].strip() == "":
                    player_career[k] = every.strip("       ")
                k = k + 1
            while ("" in player_career):
                player_career.remove("")
            k = 0
            for every in player_career:
                player_career[k] = every.lstrip("       ")
                k = k + 1

            incremnt_by = int(len(player_career) / self.base_column)
            remove_val = 0
            del player_career[remove_val:incremnt_by]
#Appending the data scraped
#putting the stats together such as G, AV, QBrec, Cmp etc.
#to finalize the consistency of the code with other solutions.
            split_lists = [player_career[x:x + incremnt_by] for x in range(0, len(player_career), incremnt_by)]
            player_career.clear()
            for each_list in split_lists:
                del each_list[1:len(each_list) - 1]
                for element in each_list:
                    player_career.append(element)
            index = 0
            for index in range(index, len(player_career), 2):
                try:
                    self.list_data[item][player_career[index]] = player_career[index + 1]
                except:
                    print("Error no index :" + str(index))


    def spider_closed(self, spider):
        print(self.list_data)

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(PlayerSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signals.spider_closed)
        return spider

