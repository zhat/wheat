import urllib.request
import urllib
from celery import shared_task
from bs4 import BeautifulSoup
from .models import BaseInfo
from datetime import datetime


@shared_task
def add(x, y):
	return x + y

@shared_task
def mul(x, y):
	return x * y

@shared_task
def xsum(numbers):
	return sum(numbers)

@shared_task
def get_shares():
	page = 1
	today = datetime.now()
	date = today.strftime("%Y-%m-%d")
	while True:
		url = r"http://q.10jqka.com.cn/index" \
			  r"/index/board/all/field/zdf/order/desc/page/{}/ajax/1/".format(page)
		print(url)
		headers = {
			'User-Agent': r'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
	# Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36		
	# 'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
			'Connection': 'keep-alive'
		}
		req = urllib.request.Request(url, headers=headers)
		page_data = urllib.request.urlopen(req).read()
		page_data = page_data.decode('gbk')
		# '/html/body/table/tbody/tr[1]/td[2]/a'
		# response = urllib.request.urlopen(url)
		# print(response)
		# print(response.getcode())
		# page = response.read()
		soup = BeautifulSoup(page_data)
		# print(page_data)
		tbody = soup.find('tbody')
		trs = tbody.find_all('tr')
		print(soup.prettify())
		print(type(tbody))
		print(type(soup))
		print('trs',type(trs[0]))
		for tr in trs:
			tds = tr.find_all('td')
			code = tds[1].get_text()
			url = tds[1].a['href']
			name = tds[2].get_text()
			new_share_dict = {'date':date,'code':code,'name':name,'url':url,'present_price':tds[3].string,
			 'range':tds[4].string,'price_range':tds[5].string,'rise_speed':tds[6].string,
			 'change_hands':tds[7].string,'volume_ratio':tds[8].string,'amplitude':tds[9].string,
			 'turnover':tds[10].string, 'floating_stock':tds[11].string,
			 'circulation_market_value':tds[12].string,'pe_ratio':tds[13].string}
			#print(tds)
			print(new_share_dict)
			new_share = BaseInfo.objects.create(**new_share_dict)
		page += 1
		if page>161:
			break

def get_detail():
	url = "http://stockpage.10jqka.com.cn/600027/"
	headers = {
		'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
					  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
		# 'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
		'Connection': 'keep-alive'
	}
	req = urllib.request.Request(url, headers=headers)
	page_data = urllib.request.urlopen(req).read()
	print(page_data)
	page_data = page_data.decode('utf-8')
	soup = BeautifulSoup(page_data)
	print(soup)
	dl = soup.find_all('dl',class_="company_details")[0]
	dds = dl.find_all('dd')
	print(dds)
	ul = soup.find_all('ul',class_="new_trading")
	print(ul)
	#print(page_data)
"""
class BaseInfo(models.Model):
    date = models.CharField("日期",max_length=64)
    code = models.CharField("代码",max_length=64)
    name = models.CharField("名称",max_length=255)
    present_price = models.CharField("现价",max_length=64,null=True)
    range = models.CharField("涨跌幅",max_length=64,null=True)
    price_range = models.CharField("涨跌",max_length=64,null=True)
    rise_speed = models.CharField("涨速",max_length=64,null=True)
    change_hands = models.CharField("换手",max_length=64,null=True)
    volume_ratio = models.CharField("量比",max_length=64,null=True)
    amplitude = models.CharField("振幅",max_length=64,null=True)
    turnover = models.CharField("成交额",max_length=64,null=True)
    floating_stock = models.CharField("流通股",max_length=64,null=True)
    circulation_market_value = models.CharField("流通市值",max_length=64,null=True)
    pe_ratio = models.CharField("市盈率",max_length=64,null=True)
    create_time = models.DateTimeField("创建时间",auto_now_add=True)
    update_time = models.DateTimeField("更新时间",auto_now=True)"""
