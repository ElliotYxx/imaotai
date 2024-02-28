import configparser

import os
import config as cf
import process

config = configparser.ConfigParser()  # 类实例化


def get_credentials_path():
    if cf.CREDENTIALS_PATH is not None:
        return cf.CREDENTIALS_PATH
    else:
        home_path = os.path.expanduser("~")
        path = os.path.join(home_path, '.imaotai', 'credentials')
        # 尝试创建目录
        try:
            os.mkdir(os.path.join(home_path, '.imaotai'))
        except OSError:
            pass
        return path


path = get_credentials_path()
config.read(get_credentials_path())
sections = config.sections()


def get_location():
    while 1:

        location = input(f"请输入你的位置，例如[小区名称]，为你自动预约附近的门店:").lstrip().rstrip()
        selects = process.select_geo(location)

        a = 0
        for item in selects:
            formatted_address = item['formatted_address']
            province = item['province']
            print(f'{a} : [地区:{province},位置:{formatted_address}]')
            a += 1
        user_select = input(f"请选择位置序号,重新输入请输入[-]:").lstrip().rstrip()
        if user_select == '-':
            continue
        select = selects[int(user_select)]
        formatted_address = select['formatted_address']
        province = select['province']
        print(f'已选择 地区:{province},[{formatted_address}]附近的门店')
        return select


if __name__ == '__main__':

    while 1:
        process.init_headers()
        # location_select: dict = get_location()
        # province = location_select['province']
        # city = location_select['city']
        # location: str = location_select['location']
        # privince = '上海市'
        # city = '上海市'
        # lat = '31.213796'
        # lng = '121.360117'

        # 地址写死
        privince = input("输入省份[福建省]:").lstrip().rstrip()
        city = input("输入城市[福州市]:").lstrip().rstrip()
        lat = input("输入经度[26.024012]:").lstrip().rstrip()
        lng = input("输入维度[119.282268]:").lstrip().rstrip()

        mobile = input("输入手机号[13812341234]:").lstrip().rstrip()
        process.get_vcode(mobile)
        code = input(f"输入 [{mobile}] 验证码[1234]:").lstrip().rstrip()
        token, userId = process.login(mobile, code)
        if mobile not in sections:
            config.add_section(mobile)  # 首先添加一个新的section
            config.set(mobile, 'province', privince)
            config.set(mobile, 'city', city)
            config.set(mobile, 'lat', lat)
            config.set(mobile, 'lng', lng)

        config.set(mobile, 'token', str(token))
        config.set(mobile, 'userId', str(userId))
        config.write(open(path, 'w+'))  # 保存数据
        condition = input(f"是否继续添加账号[Y/N]:").lstrip().rstrip()
        condition = condition.lower()
        if condition == 'n':
            break
