import requests
from bs4 import BeautifulSoup
import time
headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) " +
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}
with open("F:/data.txt", 'a+',encoding='UTF-8') as file:
    for a in range(0, 4):
        link = 'https://beijing.anjuke.com/sale/p' + str(a+1)
        r = requests.get(link, headers=headers)
        print("*******************现在在爬取第" + str(a + 1) + "页数据**********************")
        soup = BeautifulSoup(r.text, 'lxml')
        house_list = soup.find_all('li', class_="list-item")
        for i in house_list:
            name = i.find("div", class_="house-title").a.text.strip()
            price = i.find('span', class_='price-det').text.strip()
            price_area = i.find('span', class_='unit-price').text.strip()
            no_room = i.find('div', class_='details-item').span.text
            area = i.find('div', class_='details-item').contents[3].text
            floor = i.find('div', class_='details-item').contents[5].text
            year = i.find('div', class_='details-item').contents[7].text
            address = i.find('span', class_='comm-address').text.strip()
            broker = i.find('span', class_='broker-name broker-text').text.strip()
            print("\t房屋的名称：", name)
            print("价格：", price)
            print("均价：", price_area)
            print("几室几厅：", no_room)
            print("房屋面积：", area)
            print("几层楼：", floor)
            print("建造年限：", year)
            print("所在地址：", address)
            print("房屋中介：", broker)
            print("\n")
            file.write(name)
            file.write(price)
            file.write(price_area)
            file.write(no_room)
            file.write(area)
            file.write(floor)
            file.write(year)
            file.write(address)
            file.write(broker)
            file.write("\n")
#file.close()
   # print("\n房屋中介：", broker)
