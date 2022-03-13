import csv

# 将信息创建成一个列表，之后再处理成字典形式
district = []
position = []
room_name = []

# 因为已经统一好了编码格式，所以这里我们直接将字典写出
city_d = {"天津": 2}
lease_way_d = {'整租': 1, '合租': 2}
orientation_d = {'NULL': 0, '东': 1, '南': 2, '西': 3, '北': 4, '东北': 5, '东南': 6, '西北': 7, '西南': 8}
rent_way_d = {'NULL': 0, '季付价': 1, '年付价': 2, '月付价': 3, '半年付价': 4, '双月付价': 5}
check_in_time_d = {'NULL': 0, '具体入住': 1, '随时入住': 2}
viewing_time_d = {'NULL': 0, '只能周末看房': 1, '需提前预约': 2, '随时可看': 3, '一般下班后可看': 4}
lift_d = {'NULL': 0, '无': 1, '有': 2}
parking_space_d = {'NULL': 0, '免费使用': 1, '租用车位': 2}
water_d = {'NULL': 0, '民水': 1, '商水': 2}
electricity_d = {'NULL': 0, '民电': 1, '商电': 2}
gas_d = {'NULL': 0, '无': 1, '有': 2}
heating_d = {'NULL': 0, '集中供暖': 1, '自采暖': 2}
room_floor_d = {'低楼层': 1, '中楼层': 2, '高楼层': 3, '地下室': -1, '未知': -2}

# 打开我们要处理的文件
with open("Originally_Data.csv", "r", newline="") as csv_in_file:
    # 因为在之前的文件中，我忘记把总楼层和所在楼层分离开，所以这里做一下分离
    # 并将分离后的数据命名为租房信息2.0.2
    with open("Originally_Data(Floor_Separate).csv", "w", newline="") as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter=",")
        filewriter = csv.writer(csv_out_file, delimiter=",")
        # 写入表头
        header_list = ["房屋编号", "城市", "区", "方位", "房屋名", "大小", "租赁方式", "朝向", "月租", "计费方式", "几室", "几厅", "几卫", "入住", "租期", "看房", "所在楼层", "总楼层", "电梯", "车位", "用水", "用电", "燃气", "供暖"]
        filewriter.writerow(header_list)
        for row_list in filereader:
            # 将所在楼层和总楼层分离开
            row_list.insert(17, row_list[16][row_list[16].find("/") + 1:])
            row_list[16] = row_list[16][ : row_list[16].find("/")]
            # 跳过表头
            if "房屋编号" not in row_list[0]:
                filewriter.writerow(row_list)
    # 打开处理后要保存的文件
    with open("After_Processing_Data.csv", "w", newline="") as csv_out_file:
        # 将文件指针重新指向文件头
        csv_in_file.seek(0, 0)
        filereader = csv.reader(csv_in_file, delimiter=",")
        filewriter = csv.writer(csv_out_file, delimiter=",")
        # 将表头写入文件中
        header_list = ["城市", "区", "方位", "房屋名", "大小", "租赁方式", "朝向", "月租", "计费方式", "几室", "几厅", "几卫", "入住", "租期", "看房", "所在楼层", "总楼层", "电梯", "车位", "用水", "用电", "燃气", "供暖"]
        filewriter.writerow(header_list)
        for row_list in filereader:
            # 跳过表头
            if "房屋编号" in row_list[0]:
                continue
            # 下面的意思是，如果信息没有在列表中出现过，就将这个信息加入列表中
            if row_list[2] not in district:
                district.append(row_list[2])
            if row_list[3] not in position:
                position.append(row_list[3])
            if row_list[4] not in room_name:
                room_name.append(row_list[4])
        # 将列表转换成字典的形式
        i = 1
        district_d = dict.fromkeys(district)
        # 依次给字典赋值
        for district1 in district:
            district_d[district1] = i
            i += 1
        i = 1
        position_d = dict.fromkeys(position)
        for position1 in position:
            position_d[position1] = i
            i += 1
        i = 1
        room_name_d = dict.fromkeys(room_name)
        for room_name1 in room_name:
            room_name_d[room_name1] = i
            i += 1
        i = 1
        # 将编码规则保存进相应的文件中
        with open("Encoding_Rules.csv", "w") as f:
            f.write(str(city_d) + "\n" + str(district_d) + "\n" +
                    str(position_d) + "\n" + str(room_name_d) +
                    "\n" + str(lease_way_d) + "\n" + str(orientation_d) +
                    "\n" + str(rent_way_d) + "\n" +
                    str(check_in_time_d) + "\n" + str(viewing_time_d) +
                    "\n" + str(room_floor_d) + "\n" +
                    str(lift_d) + "\n" + str(parking_space_d) +
                    "\n" + str(water_d) + "\n" +
                    str(electricity_d) + "\n" + str(gas_d) +
                    "\n" + str(heating_d) + "\n" +
                    str(room_floor_d) + "\n")
        # 将文件指针重新指向文件头
        csv_in_file.seek(0, 0)
        # 处理每一项的信息
        for row_list in filereader:
            # 跳过表头
            if "房屋编号" in row_list[0]:
                continue
            # 城市全为天津，即2
            row_list[1] = 2
            # 处理区
            row_list[2] = district_d[row_list[2]]
            # 处理方位
            row_list[3] = position_d[row_list[3]]
            # 处理房屋名
            row_list[4] = room_name_d[row_list[4]]
            # 处理大小
            row_list[5] = int(row_list[5][: row_list[5].find("㎡")])
            # 处理租赁方式
            row_list[6] = lease_way_d[row_list[6]]
            # 处理朝向
            if "/" in row_list[7]:
                row_list[7] = row_list[7][: row_list[7].find("/")]
            elif "暂无" in row_list[7]:
                row_list[7] = "NULL"
            row_list[7] = orientation_d[row_list[7]]
            # 处理月租
            row_list[8] = int(row_list[8][: row_list[8].find("元")])
            # 处理计费方式
            row_list[9] = rent_way_d[row_list[9]]
            # 处理几室
            if "NULL" not in row_list[10]:
                row_list[10] = int(row_list[10][: row_list[10].find("室")])
            else:
                row_list[10] = 0
            # 处理几厅
            if "NULL" not in row_list[11]:
                row_list[11] = int(row_list[11][: row_list[11].find("厅")])
            else:
                row_list[11] = 0
            # 处理几卫
            if "NULL" not in row_list[12]:
                row_list[12] = int(row_list[12][: row_list[12].find("卫")])
            else:
                row_list[12] = 0
            # 处理入住
            if "随时入住" in row_list[13]:
                row_list[13] = "随时入住"
                row_list[13] = check_in_time_d[row_list[13]]
            elif "暂无" in row_list[13]:
                row_list[13] = "NULL"
                row_list[13] = check_in_time_d[row_list[13]]
            else:
                row_list[13] = "具体入住"
                row_list[13] = check_in_time_d[row_list[13]]
            # 处理租期，将年转化成月，取最大值
            if ("~" in row_list[14] and "月" in row_list[14]):
                row_list[14] = int(row_list[14][row_list[14].find("~") + 1 : row_list[14].find("个")])
            elif ("~" in row_list[14] and "年" in row_list[14]):
                row_list[14] = int(row_list[14][row_list[14].find("~") + 1 : row_list[14].find("年")])
                row_list[14] = int(12 * int(row_list[14]))
            elif "年" in row_list[14]:
                row_list[14] = int(row_list[14][ : row_list[14].find("年")])
                row_list[14] = int(12 * int(row_list[14]))
            elif "NULL" in row_list[14]:
                row_list[14] = 0
            else:
                row_list[14] = int(row_list[14][ : row_list[14].find("个")])
            # 处理看房
            row_list[15] = viewing_time_d[row_list[15]]
            # 把楼层信息分离开
            row_list.insert(17, int(row_list[16][row_list[16].find("/") + 1 : row_list[16].rfind("层")]))
            row_list[16] = row_list[16][ : row_list[16].find("/")]
            if "未知" in row_list[16]:
                row_list[16] = row_list[16]
            # 将具体的所在楼层转换成相应的高楼层，中楼层，低楼层
            elif ("高楼层" not in row_list[16] and "中楼层" not in row_list[16] and "低楼层" not in row_list[16]):
                level0 = 0
                level1 = int(row_list[16]) // 3
                level2 = int(row_list[16]) // 3 * 2
                level3 = int(row_list[16])
                if (int(row_list[16]) > level0 and int(row_list[16]) <= level1):
                    row_list[16] = "低楼层"
                elif (int(row_list[16]) > level1 and int(row_list[16]) <= level2):
                    row_list[16] = "中楼层"
                elif (int(row_list[16]) > level2 and int(row_list[16]) <= level3):
                    row_list[16] = "高楼层"
            else:
                row_list[16] = row_list[16]
            row_list[16] = room_floor_d[row_list[16]]
            # 处理电梯
            row_list[18] = lift_d[row_list[18]]
            # 处理车位
            row_list[19] = parking_space_d[row_list[19]]
            # 处理用水
            row_list[20] = water_d[row_list[20]]
            # 处理用电
            row_list[21] = electricity_d[row_list[21]]
            # 处理燃气
            row_list[22] = gas_d[row_list[22]]
            # 处理供暖
            row_list[23] = heating_d[row_list[23]]
            # 因为房屋编号不计入最后保存的文件，所以删除第一列
            row_list.pop(0)
            filewriter.writerow(row_list)
