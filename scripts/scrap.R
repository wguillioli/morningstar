
require(rvest)

url <- "https://global.morningstar.com/es/inversiones/fondos/0P0001EEFV/"

url2 <- "https://fundresearch.fidelity.com/mutual-funds/summary/315911750"

html_data <- read_html("https://www.azlyrics.com/b/beatles.html")

html_data <- read_html(url2)

links <- html_data %>% 
  html_nodes("a")

links

urls <- links %>% html_attr("href")

urls

# scrape all div tags
html_data %>% html_nodes("div")

# scrape header h1 tags
html_data %>% html_nodes("h1")

urls <- links %>% html_attr("href")

urls

html_data %>% html_nodes("div") %>% html_attr("id")



site = "https://www.azlyrics.com/b/beatles.html"

session <- html_session(site)

session %>% follow_link(3)

session %>% follow_link("Sun")

https://www.google.com/search?q=r+web+scraping+if+page+is+not+html&oq=r+web+scraping+if+page+is+not+html&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRigATIHCAUQIRifBTIHCAYQIRifBdIBCDc0NzZqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8

https://www.r-bloggers.com/2019/07/beautifulsoup-vs-rvest/
  
  

