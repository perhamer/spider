import random

from bs4 import BeautifulSoup
from pip._vendor import requests

from excel_export import export

headers = {
    'Cookie': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


def iqiyi_spider(key):
    result = []
    for page in range(0,35):
        target_url = "https://so.iqiyi.com/so/q_" + str(key) + "_ctg__t_0_page_" + str(
            page) + "_p_1_qc_0_rd__site_iqiyi_m_1_bitrate__af_0"
        r = requests.get(target_url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        a = soup.findAll('a', {'class': 'main-tit'})
        for i in a:
            if 'www.iqiyi.com' in i.get('href') and 'html' in i.get('href'):
                url = str(i.get('href')).replace("//", "")
                if not url.startswith("http://"):
                    url = "http://"+url
                row = [url, i.get('title')]
                result.append(row)
        print(page)
    print("查找完毕")
    export(result)
    print("导出完毕")


if __name__ == '__main__':
    iqiyi_spider("亮剑")
