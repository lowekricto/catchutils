import cv2
import os


def getinfo(path):
    try:
        cap = cv2.VideoCapture(path)
        # 帧率
        fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
        # 分辨率-宽度
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # 分辨率-高度
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # 总帧数
        frame_counter = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    except:
        return 0, 0
    return width, height


# 获取指定文件夹下的文件夹名称
def get_dir_name(path):
    dir_name = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if (dir.find('Season') != -1):
                continue
            if (dir.find('S0') != -1):
                continue
            if (dir.find('ass') != -1):
                continue
            if (dir.find('Bonus') != -1):
                continue
            if (dir.find('OVA') != -1):
                continue
            if (dir.find('Scans') != -1):
                continue
            if (dir.find('OAD06') != -1):
                continue
            dir_name.append(dir)
    return dir_name


# 获取指定文件夹下的所有文件名
def get_file_name(path):
    file_name = []
    for root, dirs, files in os.walk(path):
        for file in files:

            file_name.append(file)
    return file_name


def main(path):
    nofomat = []
    dirs = get_dir_name(path)
    for x in dirs:
        folder = path+"\\"+x
        files = get_file_name(folder)
        for y in files:
            file = folder+"\\"+y

            w, h = getinfo(file)
            if w < 1920 and h < 1080:
                nofomat.append(x)
                break

    # 保存noformat的内容到文件 UTF-8
    with open('noformat.txt', 'w', encoding='utf-8') as f:
        for x in nofomat:
            try:
                f.write(x + '\n')
            except:
                pass
    return nofomat


print(main('Z:\\A_ACGN\\A_动漫'))
