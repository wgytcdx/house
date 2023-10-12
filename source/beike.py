# encoding:utf-8

from html.parser import HTMLParser

class BeikeParser(HTMLParser):
    def __init__(self):
        super().__init__()
        # 存储中间数据（链家为总房价与单价）
        self.span = ""
        # 房屋名称
        self.houseName = []

        # 小区名称
        self.villageName = []
        # 小区均价
        self.price = []
        # 小区名称 小区所在区
        self.villageAdd1 = []
        # 小区名称 小区所在区
        self.villageAdd2 = []
        # 房子介绍 小区所在街道
        self.houseNote = []
        # 总价
        self.houseTotlePrice = []
        self.houseTotlePrice_tmp = "" #用于拼接houseTotlePrice
        # 单价
        self.houseUnitPrice = []
        # 房屋链接
        self.houseLink = []
        # 第一张图片
        self.houseImg = []
        # 关注人数
        self.followNum = []
        # 用于标记数据类型
        self.flag = []
        self.sign = 0

    def feed(self, data):
        super().feed(data)
        # 校验数据个数是否统一
        size = len(self.houseName)
        # if len(self.houseName) != size or len(self.villageName) != size or len(self.houseNote) != size \
        #         or len(self.houseTotlePrice) != size or len(self.houseUnitPrice) != size or len(self.houseLink) != size \
        #         or len(self.houseImg) != size or len(self.followNum) != size:
        #     raise ValueError("数据个数不一致：houseName-" + str(len(self.houseName)) + ",villageName-" + str(len(self.villageName)) +
        #                      ",houseNote-" + str(len(self.houseNote)) + ",houseTotlePrice-" + str(len(self.houseTotlePrice)) +
        #                      ",houseUnitPrice-" + str(len(self.houseUnitPrice)) + ",houseLink-" + str(len(self.houseLink)) +
        #                      ",houseImg-" + str(len(self.houseImg)) + ",followNum-" + str(len(self.followNum)))
        
        # file = open('output.txt', 'w')
        # file.write(data)
        # file.close()
        # print(data.houseName)
        return self.villageName, self.price, self.villageAdd1, self.villageAdd2

    def handle_starttag(self, tag, attrs):
        if tag == "div" and ("class", "totalPrice") in attrs:
            self.flag.append("price")
        elif tag == "div" and ("class", "totalPrice noPrice") in attrs:
            self.flag.append("price")
        elif tag == "a" and ("class", "maidian-detail") in attrs:
            # print(attrs)
            # self.flag.append("houseName")
            for attr in attrs:
                if attr[0] == "title":
                    self.villageName.append(attr[1])
                # elif attr[0] == "href":
                #     self.houseLink.append(attr[1])
        # elif tag == "a" and ("data-el", "region") in attrs:
        #     self.flag.append("villageName")
        # elif tag == "a" and ("class", "no_resblock_a") in attrs:
        #     self.flag.append("villageName")
        # elif tag == "div" and ("class", "houseInfo") in attrs:
        #     self.flag.append("houseNote")
        elif tag == "a" and ("class", "district") in attrs:
            for attr in attrs:
                if attr[0] == "title":
                    self.villageAdd1.append(attr[1].replace('小区',''))
            # self.flag.append("villageName")
        elif tag == "a" and ("class", "bizcircle") in attrs:
            for attr in attrs:
                if attr[0] == "title":
                    self.villageAdd2.append(attr[1].replace('小区',''))
            # self.flag.append("houseNote")
        # elif tag == "img" and ("class", "lj-lazy") in attrs:
        #     for attr in attrs:
        #         if attr[0] == "alt":
        #             for attr2 in attrs:
        #                 if attr2[0] == "data-original":
        #                     self.houseImg.append(attr2[1])
        #                     break
        #             break
        # elif tag == "div" and ("class", "positionInfo") in attrs:
        #     self.flag.append("villageName_1")
        # elif tag == "a" and len(self.flag) > 0 and self.flag[-1] == "villageName_1":
        #     self.flag.pop()
        #     self.flag.append("villageName_2")
        # elif tag == "div" and ("class", "followInfo") in attrs:
        #     self.flag.append("followNum")

    def handle_data(self, data):
        data = data.replace(' ', '')
        if len(self.flag) > 0:
            if self.flag[-1] == "price":
                print(data)
                if data:
                    self.price.append(data)
                else: 
                    self.price.append('暂无数据')
                print(data)
                self.flag.pop()
                    # self.houseTotlePrice_tmp = self.span
                    # self.villageName.append(self.span.split('|')[0].strip())
            # elif self.flag[-1] == "houseName":
            #     # print(str(data))
            #     self.houseName.append(data)
            #     self.flag.pop()
            # elif self.flag[-1] == "villageName":
            #     # print(str(data))
            #     self.villageName.append(data)
            #     self.flag.pop()
            # elif self.flag[-1] == "houseNote":
            #     print(self.span)
            #     self.houseNote.append(self.span)
            #     self.villageName.append(self.span.split('|')[0])
            #     self.span = ""
            #     self.flag.pop()
            # elif self.flag[-1] == "houseTotlePrice_2":
            #     if data != "":
            #         self.houseTotlePrice_tmp = self.houseTotlePrice_tmp + self.span + data
            #     self.span = ""
            #     # self.flag.pop()
            # elif self.flag[-1] == "villageName_2":
            #     # print(str(data))
            #     self.villageName.append(data)
            #     self.flag.pop()

    def handle_endtag(self, tag):
        if tag == "div" and len(self.flag) > 0 and self.flag[-1] == "houseTotlePrice_2":
            self.houseTotlePrice.append(self.houseTotlePrice_tmp)#.replace(' ', ''))
            self.houseTotlePrice_tmp = ""
            self.flag.pop()

