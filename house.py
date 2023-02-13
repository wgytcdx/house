# encoding:utf-8
# python3.0

from source.save import saveData
from source.common import getHtml
from source.report import reportData
import configparser
import webbrowser
import os


# ------主函数------
# delete()
if __name__ == '__main__':
    # 获取参数
    config = configparser.ConfigParser()
    config.read("config.ini")

    # 清除数据
    save = saveData(config)
    save.deleteOldData()

    # 贝壳找房 （例：江北万达 天沁、天悦、三江官邸） 根据自己需求添加链接
    beike1 = getHtml('''https://nb.ke.com/ershoufang/l3c4420029837662661/?sug=%E5%A4%A9%E6%B2%81%E5%AE%B6%E5%9B%AD''')
    beike2 = getHtml('''https://nb.ke.com/ershoufang/rs%E5%A4%A9%E6%82%A6%E5%AE%B6%E5%9B%AD/''')
    beike3 = getHtml('''https://nb.ke.com/ershoufang/rs%E5%A4%A9%E6%82%A6%E5%AE%B6%E5%9B%AD/''')
    beike_htmls = [beike1,beike2,beike3]
    for beike_html in beike_htmls:
        save.beike_save(beike_html)

    # 链家 （例：江北万达 天沁、天悦、三江官邸） 根据自己需求添加链接
    lianjia1 = getHtml('''https://nb.lianjia.com/ershoufang/l3c4420029837662661/?sug=%E5%A4%A9%E6%B2%81%E5%AE%B6%E5%9B%AD''')
    lianjia2 = getHtml('''https://nb.lianjia.com/ershoufang/l2l3rs%E5%A4%A9%E6%82%A6%E5%AE%B6%E5%9B%AD/''')
    lianjia3 = getHtml('''https://nb.lianjia.com/ershoufang/l3l4c4420044001039597/?sug=%E5%AE%9D%E6%97%AD%E8%A7%82%E9%82%B8''')
    lianjia_htmls = [lianjia1,lianjia2,lianjia3]
    for lianjia_html in lianjia_htmls:
        save.lianjia_save(lianjia_html)

    # 无效
    # 58同城 高江北万达枫华里 三室、二室 第一页、第二页、第三页 
    tongcheng1 = getHtml('''https://nb.58.com/ershoufang/?comm_id=2446170&q=%E4%B8%AD%E6%B5%B7%E6%9E%AB%E6%A1%A5%E9%87%8C''')
    tongcheng2 = getHtml('''https://nb.58.com/ershoufang/p2/?comm_id=2446170&q=%E4%B8%AD%E6%B5%B7%E6%9E%AB%E6%A1%A5%E9%87%8C&PGTID=0d30000c-0008-7942-596a-07f450a07a11&ClickID=1''')
    # tongcheng3 = getHtml('''http://bj.58.com/ershoufang/pn3/?comm_id=2446170&q=中海枫桥里&huansuanyue=200_600&bunengdaikuan=0&area=60_100&PGTID=0d300000-0000-08f9-ba56-6673c850e2b8&ClickID=1''')
    print(str(tongcheng1.encode('GB18030')))
    tongcheng_htmls = [tongcheng1, tongcheng2]
    # for tongcheng_html in tongcheng_htmls:
    #     save.tongcheng_save(tongcheng_html)

    # 有验证码
    # 安居客 （例：北京 200-600万 60-100平 按最新排序） 根据自己需求添加链接
    anjuke1 = getHtml('''https://nb.anjuke.com/sale/?comm_id=1068474&q=%E4%B8%AD%E6%B5%B7%E6%9E%AB%E6%A1%A5%E9%87%8C''')
    anjuke2 = getHtml('''https://nb.anjuke.com/sale/p2/?comm_id=1068474&q=%E4%B8%AD%E6%B5%B7%E6%9E%AB%E6%A1%A5%E9%87%8C''')
    anjuke3 = getHtml('''https://nb.anjuke.com/sale/p3/?comm_id=1068474&q=%E4%B8%AD%E6%B5%B7%E6%9E%AB%E6%A1%A5%E9%87%8C''')
    anjuke4 = getHtml('''https://nb.anjuke.com/sale/p4/?comm_id=1068474&q=%E4%B8%AD%E6%B5%B7%E6%9E%AB%E6%A1%A5%E9%87%8C''')
    anjuke_htmls = [anjuke1, anjuke2, anjuke3,anjuke4]
    for anjuke_html in anjuke_htmls:
        save.anjuke_save(anjuke_html)

    # 报错
    # # 赶集 高新园区 80-120W 3室 精装修
    # ganji1 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3q2/''')
    # ganji2 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3o2q2/''')
    # ganji3 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3o3q2/''')
    # ganji_htmls = [ganji1, ganji2, ganji3]
    # for ganji_html in ganji_htmls:
    #     ganji_save(ganji_html)

    print("生成报告中...")
    rep = reportData()
    reportFileName = rep.get_report()
    webbrowser.open('''file:///''' + os.path.dirname(__file__) + '''/reports/''' + reportFileName)

    print("OVER!!!")
