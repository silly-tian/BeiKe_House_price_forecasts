from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

# 先保存要爬取的网页的基本部分
base_url = "https://tj.zu.ke.com/zufang/"
# 删除原文件的数据后在保存的文件中写入表头
with open("Originally_Data1.csv", "w+") as f:
    f.write("房源编号,城市,区,方位,房屋名,大小,租赁方式,朝向,月租,计费方式,"
            "几室,几厅,几卫,入住,租期,看房,楼层,"
            "电梯,车位,用水,用电,燃气,供暖\n")
# 这个循环遍历的是网页的1到50页
for n in range(1, 51):
    base_url1 = base_url + "pg%d/" % n
    # 打开相应的页数的网址
    base_html = urlopen(base_url1).read().decode('utf-8')
    soup = BeautifulSoup(base_html, features='lxml')
    # 寻找网址下的子网址
    url_divs = soup.find("div", {"class": "content__list"})
    url_divss = url_divs.find_all("div", {"class": "content__list--item"})
    for url_div in url_divss:
        list1 = url_div.find("p", {"class": "content__list--item--des"})
        # list_data为区，方位，房屋名的数据
        list_data = list1.find_all("a")
        # 将区，方位,房屋名的信息保存下来
        district = list_data[0].get_text()
        position = list_data[1].get_text()
        room_name = list_data[2].get_text()
        # 找到子网址
        url = url_div.find("a", {"class" : "content__list--item--aside"})
        url_url = url['href']
        url_url = "https://tj.zu.ke.com" + url_url
        # 打开相应的子网址
        html = urlopen(url_url).read().decode('utf-8')
        soup2 = BeautifulSoup(html, features='lxml')
        # 寻找房源编号
        number = soup2.find("i", {"class": "house_code"}).get_text()
        number = number[5:]
        # 寻找标题
        title1 = soup2.find("title").get_text()
        # 寻找租赁方式
        lease_way = title1[: title1.find("·")]
        # 寻找地址
        adress = soup2.find("p", {"class": "bread__nav__wrapper oneline"})
        adress1 = adress.find_all("a")
        city = adress1[0].get_text()
        city = city[:city.find("贝壳")]
        # 寻找月租
        rent = soup2.find("p", {"class" : "content__aside--title"}).get_text()
        # 将月租和计费方式分开
        if "(" in rent:
            rent_way = rent[rent.find("(") + 1: rent.find(")")]
        else:
            rent_way = "NULL"
        rent = rent[1: rent.find("月") + 1]
        # 寻找面积
        data = soup2.find("p", {"class": "content__article__table"})
        data1 = data.find_all("span")
        area = data1[2].get_text()
        # 寻找朝向
        orientation = data1[3].get_text()
        orientation = orientation[1:]
        orientation = orientation.replace(" ", "/")
        # 寻找室，厅，卫
        room = data1[1].get_text()
        rooms = room[:room.find("室") + 1]
        if "0" in rooms:
            rooms = "NULL"
        halls = room[room.find("室") + 1: room.find("厅") + 1]
        if "0" in halls:
            halls = "NULL"
        toilets = room[room.find("厅") + 1: room.find("卫") + 1]
        if "0" in toilets:
            toilets = "NULL"
        # 寻找之后的其他数据(看房,楼层,电梯,车位,用水,用电,燃气,供暖)
        base_data = soup2.find("div", {"class" : "content__article__info"})
        base_data1 = base_data.find("ul")
        base_data2 = base_data1.find_all("li")
        check_in_time = base_data2[2].get_text()
        check_in_time = check_in_time[check_in_time.find("：") + 1:]
        if "暂无数据" in check_in_time:
            check_in_time = "NULL"
        lease_term = base_data2[4].get_text()
        lease_term = lease_term[lease_term.find("：") + 1 : ]
        if "暂无数据" in lease_term:
            lease_term = "NULL"
        viewing_time = base_data2[5].get_text()
        viewing_time = viewing_time[viewing_time.find("：") + 1:]
        if "暂无数据" in viewing_time:
            viewing_time = "NULL"
        floor = base_data2[7].get_text()
        floor = floor[floor.find("：") + 1:]
        if "暂无数据" in floor:
            floor = "NULL"
        lift = base_data2[8].get_text()
        lift = lift[lift.find("：") + 1:]
        if "暂无数据" in lift:
            lift = "NULL"
        parking_space = base_data2[10].get_text()
        parking_space = parking_space[parking_space.find("：") + 1:]
        if "暂无数据" in parking_space:
            parking_space = "NULL"
        water = base_data2[11].get_text()
        water = water[water.find("：") + 1:]
        if "暂无数据" in water:
            water = "NULL"
        electricity = base_data2[13].get_text()
        electricity = electricity[electricity.find("：") + 1:]
        if "暂无数据" in electricity:
            electricity = "NULL"
        gas = base_data2[14].get_text()
        gas = gas[gas.find("：") + 1:]
        if "暂无数据" in gas:
            gas = "NULL"
        heating = base_data2[16].get_text()
        heating = heating[heating.find("：") + 1:]
        if "暂无数据" in heating:
            heating = "NULL"
        # 再次打开要保存的文件，将信息保存进文件
        with open("Originally_Data1.csv", "a+") as f:
            f.write(number + "," + city + "," + district + "," + position + "," +
                    room_name + "," + area + "," + lease_way + "," + orientation +
                    "," + rent + "," + rent_way + "," + rooms +
                    "," + halls + "," + toilets + "," + check_in_time + "," +
                    lease_term + "," + viewing_time + "," + floor + "," +
                    lift + "," + parking_space + "," + water +
                    "," + electricity + "," + gas + "," + heating + "\n")










