require 'mechanize'


url = "http://es.finance.yahoo.com/actives?e=o"

agent = Mechanize.new
p "getting url #{url}"
page = agent.get(url)
p "getting rows"
rows = page.parser.xpath("//*[@id='yfitp']/table/tbody/tr")

output = []

for row in rows
  company = {}
  p "company..."
  company['code'] = row.xpath("./td[@class='first']//a")[0].text
  company['name'] = row.xpath("./td[@class='second name']").text
  p "getting arrow"
  arrow_src = row.xpath(".//*[starts-with(@id,'yfs_c10_')]/img")[0]['src']
  p arrow_src
  m = /d\/(.*)_.\.gif/.match(arrow_src)  
  company['arrow'] = m[1]
  p "getting company"
  company['change'] = row.xpath(".//*[starts-with(@id,'yfs_c10_')]/b").text
  percent = row.xpath(".//*[starts-with(@id,'yfs_p20_')]").text
  percent = percent.gsub(/[\(\)\%]/,'')
  percent = percent.strip
  company['percent_change'] = percent
  output << company
  p company
  
end
