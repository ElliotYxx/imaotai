ITEM_MAP = {
    "10941": "53%vol 500ml贵州茅台酒（甲辰龙年）",
    "10942": "53%vol 375ml×2贵州茅台酒（甲辰龙年）",
    "10056": "53%vol 500ml茅台1935",
    "2478": "53%vol 500ml贵州茅台酒（珍品）"
}

# 需要预约的商品(默认只预约2个兔茅)
########################
ITEM_CODES = ['10941', '10942']

# push plus 微信推送,具体使用参考  https://www.pushplus.plus
# 例如： PUSH_TOKEN = '123456'
########################
# 不填不推送消息，一对一发送
PUSH_TOKEN = '60056febc89449e9bc731b52f5b08c8c'
########################

# credentials 路径，例如：CREDENTIALS_PATH = /home/user/.imaotai/credentials
# 不配置，使用默认路径，在宿主目录
# 例如： CREDENTIALS_PATH = '/home/user/.imaotai/credentials'
########################
CREDENTIALS_PATH = None
########################

# 预约规则配置
########################
# 预约本市出货量最大的门店
MAX_ENABLED = False
# 预约你的位置附近门店
DISTANCE_ENABLED = True
########################


CITY_MAP = {
    # 1 上海
    "1": {
        "province_name":"上海市",
        "city_name":"上海市",
        "lat":"31.213796",
        "lng":"121.360117"
    },
    # 2 合肥
    "2": {
        "province_name":"安徽省",
        "city_name":"合肥市",
        "lat":"31.903006",
        "lng":"117.23848"
    },
    # 3 福州
    "3": {
        "province_name":"福建省",
        "city_name":"福州市",
        "lat":"26.024012",
        "lng":"119.282268"
    },
    # 4 贵阳
    "4": {
        "province_name":"贵州省",
        "city_name":"贵阳市",
        "lat":"26.612832",
        "lng":"106.765878"
    }
}
