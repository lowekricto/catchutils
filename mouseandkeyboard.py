import pyautogui as pg


def getposition():
    # 一直获得鼠标位置
    while True:
        x, y = pg.position()
        positionStr = 'X:' + str(x).rjust(4) + ' Y:' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)


# 天刀窗口坐标组

# 清明
# pos0 = (2429, 54)
# pos1 = (2423, 186)
# pos2 = (2428, 212)
# pos3 = (2467, 213)
# pos4 = (1180, 833)

# 狗张鑫
pos0 = (1844, 28)
pos1 = (1811, 193)
pos2 = (1811, 224)
pos3 = (1890, 227)
pos4 = (871, 666)

# 黑水泽地图数据
targets = [[2502, 1170],
           [2505, 1452],
           [2495, 1116],
           [2477, 1160],
           [2466, 1198],
           [2463, 1142],
           [2461, 1094],
           [2458, 1128],
           [2448, 1422],
           [2446, 1435],
           [2436, 1274],
           [2431, 1221],
           [2387, 1099],
           [2387, 1174],
           [2380, 1364],
           [2371, 1519],
           [2361, 1228],
           [2336, 1208],
           [2332, 1105],
           [2316, 1356],
           [2313, 1606],
           [2301, 1524],
           [2300, 1105],
           [2289, 1141],
           [2257, 1350],
           [2240, 1253],
           [2234, 1449],
           [2218, 1139],
           [2185, 1227],
           [2131, 1373],
           [2458, 1503],
           [2366, 1590],
           ]
# 垂星谷地图数据
targets1 = [[1685, 1556],
            [1995, 1285],
            [1965, 1320],
            [1906, 1445],
            [1905, 1505],
            [1905, 1485],
            [1870, 1490],
            [1855, 1629],
            [1830, 1621],
            [1797, 1402],
            [1785, 1504],
            [1756, 1507],
            [1753, 1438],
            [1705, 1602],
            [1694, 1255],
            [1691, 1593],
            [1670, 1402],
            [1657, 1395],
            [1633, 1335],
            [1610, 1223],
            [1605, 1278],
            [1551, 1252],
            [1541, 1395],
            [1498, 1392],
            [1425, 1563],
            [1424, 1598],
            [1420, 1472],
            [1405, 1463],
            [1371, 1462],
            [1339, 1465],
            [1319, 1462],
            [1316, 1592],
            [1266, 1273],
            [1245, 1290],
            [1171, 1596],
            [1114, 1410],
            [989, 1128],
            [983, 1114],
            [1206, 1610],
            [1050, 1115],
            ]
# 碧落原地图数据
targets2 = [[2140, 1568],
            [1563, 2103],
            [1717, 1826],
            [1810, 2125],
            [1845, 2016],
            [1849, 1973],
            [1850, 1826],
            [1874, 1905],
            [1877, 1990],
            [1920, 2054],
            [1925, 2111],
            [1929, 1976],
            [1952, 1469],
            [1961, 1434],
            [1987, 1959],
            [2002, 1685],
            [2004, 1761],
            [2006, 2128],
            [2047, 1773],
            [2053, 1699],
            [2064, 1698],
            [2084, 1837],
            [2075, 1369],
            [2077, 1483],
            [2082, 1894],
            [2082, 1953],
            [2085, 1780],
            [2089, 1824],
            [2095, 1961],
            [2097, 1834],
            [2106, 1979],
            [2107, 1878],
            [2117, 1986],
            [2123, 2003],
            [2124, 2245],
            [2128, 2062],
            [2148, 1748],
            [2149, 1715],
            [2158, 1939],
            [2174, 1907],
            [2185, 1914],
            [2187, 1941],
            [2189, 1731],
            [2207, 1769],
            [2214, 1944],
            [2215, 1995],
            [2229, 2028],
            [2231, 1958],
            [2234, 1922],
            [2245, 1660],
            [2246, 2059],
            [2267, 1674],
            [2282, 1840],
            [2290, 1840],
            [2313, 1804],
            [2384, 1831],
            [2401, 2019],
            [2433, 1835],
            [2447, 1836],
            [2452, 2001],
            [2495, 1807],
            [2515, 1727],
            [2515, 2024],
            [2571, 1899],
            [2603, 1832],
            [2645, 1741], ]
# 行云廊
targets3 = [[1511, 2058],
            [1768, 1680],
            [1741, 1769],
            [1736, 1679],
            [1672, 1618],
            [1614, 1656],
            [1587, 1711],
            [1575, 1755],
            [1565, 1867],
            [1547, 2132],
            [1535, 1651],
            [1427, 2017],
            [1401, 1755],
            [1375, 2138],
            [1315, 1861],
            [1306, 2091],
            [1276, 1949],
            [1261, 1959],
            [1250, 1701],
            [1249, 1777],
            [1217, 2197],
            [1213, 2220],
            [1182, 2057],
            [1178, 2016],
            [1155, 1952],
            [1149, 1676],
            [1147, 1810],
            [1095, 2007],
            [1078, 1664],
            [1005, 1935],
            [998, 1884],
            [985, 1893],
            [970, 1908],
            [962, 1544],
            [909, 1997],
            [890, 2055],
            [860, 1968],
            [770, 1921],
            [752, 2000],
            [722, 1920], ]


# 执行
def todo(targets):
    for x in targets:
        y = [str(x[0]).rjust(4, '0'), str(x[1]).rjust(4, '0')]
        # 移动到坐标零
        pg.moveTo(pos0, duration=0.0)
        # 单击
        pg.click()
        # 移动到坐标一
        pg.moveTo(pos1, duration=0.0)
        # 单击
        pg.click()
        # 键盘输入坐标一
        pg.press(y[0][0])
        pg.press(y[0][1])
        pg.press(y[0][2])
        pg.press(y[0][3])
        # 移动到坐标二
        pg.moveTo(pos2, duration=0.0)
        # 单击
        pg.click()
        # 键盘输入坐标二
        pg.press(y[1][0])
        pg.press(y[1][1])
        pg.press(y[1][2])
        pg.press(y[1][3])
        # 移动到坐标三
        pg.moveTo(pos3, duration=0.0)
        # 单击
        pg.click()
        # 移动到坐标四
        pg.moveTo(pos4, duration=0.0)
        # 单击
        pg.click()


# 主函数
def main():

    while True:
        selected = input('选择地图： [1]:黑水泽 [2]:垂星谷 [3]:碧落原 [4]:行云廊  \n')
        if selected == '1':
            target = targets
        elif selected == '2':
            target = targets1
        elif selected == '3':
            target = targets2
        elif selected == '4':
            target = targets3
        else:
            print('选择错误，请重新选择')
            continue

        # 执行
        todo(target)


main()
