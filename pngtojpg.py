import os
from PIL import Image
import threading

folders = ["Azami", "Nyako喵子", "一小央泽", "南桃Momoko", "小野妹子", "曉美媽", "焖焖碳", "秋和柯基", "銘銘Kizami", "鬼畜瑶在不在w", "Bambi밤비", "PAKI酱", "一笑芳香沁", "叉子宝宝", "弥音音ww", "木绵绵OwO", "無料bot", "羊大真人", "铁板烧鬼舞w", "鳗鱼霏儿", "Byoru", "Rioko凉凉子", "一米八的大梨子", "名濑弥七", "御子Yumiko", "木花琳琳是勇者", "爱老师_PhD", "羽生三未", "镜酱", "鹿野希", "Fushii_海堂", "Sayathefox", "七月喵子", "周叽是可爱兔兔", "念念_D", "果咩酱w", "猫君君", "芋圆侑子", "阿包也是兔娘", "麻花麻花酱", "G44不会受伤", "Shika小鹿鹿", "三度_69", "啊日日_Ganlory", "抖娘_利世", "桜井宁宁", "猫田圣奈奈", "苏嫣嫣阿姨", "阿半今天很开心", "黑川", "Godzilla", "Uki雨季", "不呆猫", "塔塔_Lo1iTa", "抱走莫子aa", "桜桃喵", "王胖胖u", "菌烨tako", "阿薰kaOri", "黑猫猫OvO", "JKFUN", "Yoko宅夏", "九曲Jean", "墨玉-M", "日奈娇",
           "森萝财团", "瓜希酱", "蜜汁猫裘", "陆卿卿", "KETTOE", "izumi泉桃子", "二佐Nisa", "夏鸽鸽不想起床", "星之迟迟", "樱群", "疯猫ss", "蠢沫沫", "雪晴Astra", "Kitaro_绮太郎", "kaya萱", "五更百鬼", "奈汐酱nice", "星澜是澜澜叫澜妹呀", "樱落酱w", "白烨", "西呱呀呀呀", "雪琪SAMA", "Kuuko W", "lovely呆玄", "你的负卿", "如月灰", "星野saori", "水淼Aqua", "白金Saki", "西园寺南歌", "雯妹不讲道理", "Messie Huang", "nagisa魔物喵", "佳佳好难啊", "妖少", "星野咪兔", "沧霁桔梗", "白银81", "起司块wii", "霜月shimo", "Momoko葵葵", "vams子", "千夜未来", "小仓千代w", "是依酱呀", "洛璃LoLiSAMA", "皮皮奶可可爱了啦", "轩萧学姐", "青青子JS", "Money冷冷", "yui金鱼", "半半子", "小女巫露娜", "是本末末", "清水由乃", "眼酱大魔王w", "过期米线线喵", "面饼仙儿", "NinJA阿寨寨", "一千只猫薄禾", "南宫", "小容仔咕咕咕w", "晕崽Zz", "炸酱沐沐", "神楽坂真冬", "迷失人形QUQ", "香草喵露露"]
# folders =["qwe" ]

def webp2png(folderpath, image):
    try:
        imagename = (str(image).split('.'))[0]

        im = Image.open(folderpath+image).convert("RGB")

        im.save(folderpath+imagename+'.jpg', 'JPEG', quality=100)

        os.remove(folderpath+image)
        print('转换完成：'+folderpath+imagename+'.jpg')
    except:
        print(folderpath+image+"不存在！")


# 获得指定文件夹下所有文件的路径
def get_all_file(folderpath):

    file_list = []
    for root, dirs, files in os.walk(folderpath):
        for file in files:
            target = (root+"\\", file)
            webp2png(target[0], target[1])
    return file_list


def main(path):
    for x in folders:
        t = threading.Thread(target=get_all_file, args=(path+x, ))
        t.start()


main('Z:\\A_ACGN\\L_LSP\\')
