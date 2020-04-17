from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen

url_list = ['http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html',
            'http://books.toscrape.com/catalogue/page-3.html',
            'http://books.toscrape.com/catalogue/page-4.html',
            'http://books.toscrape.com/catalogue/page-5.html',
            'http://books.toscrape.com/catalogue/page-6.html',
            'http://books.toscrape.com/catalogue/page-7.html',
            'http://books.toscrape.com/catalogue/page-8.html',
            'http://books.toscrape.com/catalogue/page-9.html',
            'http://books.toscrape.com/catalogue/page-10.html',
            'http://books.toscrape.com/catalogue/page-11.html',
            'http://books.toscrape.com/catalogue/page-12.html',
            'http://books.toscrape.com/catalogue/page-13.html',
            'http://books.toscrape.com/catalogue/page-14.html',
            'http://books.toscrape.com/catalogue/page-15.html',
            'http://books.toscrape.com/catalogue/page-16.html',
            'http://books.toscrape.com/catalogue/page-17.html',
            'http://books.toscrape.com/catalogue/page-18.html',
            'http://books.toscrape.com/catalogue/page-19.html',
            'http://books.toscrape.com/catalogue/page-20.html',
            'http://books.toscrape.com/catalogue/page-21.html',
            'http://books.toscrape.com/catalogue/page-22.html',
            'http://books.toscrape.com/catalogue/page-23.html',
            'http://books.toscrape.com/catalogue/page-24.html',
            'http://books.toscrape.com/catalogue/page-25.html',
            'http://books.toscrape.com/catalogue/page-26.html',
            'http://books.toscrape.com/catalogue/page-27.html',
            'http://books.toscrape.com/catalogue/page-28.html',
            'http://books.toscrape.com/catalogue/page-29.html',
            'http://books.toscrape.com/catalogue/page-30.html',
            'http://books.toscrape.com/catalogue/page-31.html',
            'http://books.toscrape.com/catalogue/page-32.html',
            'http://books.toscrape.com/catalogue/page-33.html',
            'http://books.toscrape.com/catalogue/page-34.html',
            'http://books.toscrape.com/catalogue/page-35.html',
            'http://books.toscrape.com/catalogue/page-36.html',
            'http://books.toscrape.com/catalogue/page-37.html',
            'http://books.toscrape.com/catalogue/page-38.html',
            'http://books.toscrape.com/catalogue/page-39.html',
            'http://books.toscrape.com/catalogue/page-40.html',
            'http://books.toscrape.com/catalogue/page-41.html',
            'http://books.toscrape.com/catalogue/page-42.html',
            'http://books.toscrape.com/catalogue/page-43.html',
            'http://books.toscrape.com/catalogue/page-44.html',
            'http://books.toscrape.com/catalogue/page-45.html',
            'http://books.toscrape.com/catalogue/page-46.html',
            'http://books.toscrape.com/catalogue/page-47.html',
            'http://books.toscrape.com/catalogue/page-48.html',
            'http://books.toscrape.com/catalogue/page-49.html',
            'http://books.toscrape.com/catalogue/page-50.html',]

filename = 'submission.csv'
j = 0
headers = ['image_url','book_title','product_price']
with open(filename,'w',encoding='utf-8') as f:
	header_string = ','.join(headers)
	header_string += '\n'
	f.write(header_string)
	for url in url_list:
		url_data = urlopen(url)
		book_data = url_data.read()
		url_data.close()
		books_soup = Soup(book_data,'html.parser')
		book_title = books_soup.find_all('h3')
		book_img = books_soup.find_all('img')
		book_price = books_soup.find_all('p',{'class':'price_color'})
		for i in range(len(book_title)):
			rows_data = []
			rows_data.append(book_img[i].get('src'))
			rows_data.append(book_title[i].text)
			rows_data.append(book_price[i].text)
			rows_string = ','.join(rows_data)
			rows_string += '\n'
			f.write(rows_string)
			j+=1
			print(j)
	f.close()