import requests
from bs4 import BeautifulSoup

# runnerCount = {
#     "S": 0,
#     "CP1": 0,
#     "CP2": 0,
#     "CP3": 0,
#     "CP4": 0,
#     "G": 0
# }

urlFull1 = "http://www.k-sok.com/corunners/timeline?raceId=5617"
urlHalf1 = "http://www.k-sok.com/corunners/timeline?raceId=5618"
urlFull2 = "http://www.k-sok.com/corunners/timeline?raceId=5620"
urlHalf2 = "http://www.k-sok.com/corunners/timeline?raceId=5619"


def scrape(runnerCount, url):
    outputTr = []
    res = requests.get(url)
    bs = BeautifulSoup(res.text, 'html.parser')
    table = bs.select("table.list")[2]
    # print(table.select("tr"))
    for tr in table.select("tr"):
        tds = list(tr.select("td"))
        # フォーマットエラー
        if len(tds) < 4:
            continue
        # 必要情報だけ出力
        # outputTr.append("<tr>"+tds[0].string+tds[1].string +
        #                 tds[2].string+tds[3].string+"</tr>")
        trClass = " ".join(tr['class'])
        outputTr.append(
            f'<tr class="{trClass}"> '+str(tds[0])+str(tds[1])+str(tds[2])+str(tds[3])+" </tr >")
        # 棄権はカウントに含まない
        if tds[0].text.startswith("途中棄権"):
            continue
        # print(tr.select("td")[3])
        cpText = tds[3].text
        # print(cpText)
        if cpText.startswith("スタート"):
            runnerCount["S"] += 1
        elif cpText.startswith("CP1"):
            runnerCount["CP1"] += 1
        elif cpText.startswith("CP2"):
            runnerCount["CP2"] += 1
        elif cpText.startswith("CP3"):
            runnerCount["CP3"] += 1
        elif cpText.startswith("CP4"):
            runnerCount["CP4"] += 1
        elif cpText.startswith("CP１"):
            runnerCount["CP1"] += 1
        elif cpText.startswith("CP２"):
            runnerCount["CP2"] += 1
        elif cpText.startswith("CP３"):
            runnerCount["CP3"] += 1
        elif cpText.startswith("CP４"):
            runnerCount["CP4"] += 1
        elif cpText.startswith("ゴール"):
            runnerCount["G"] += 1
    return "<table><tbody>" + "".join(outputTr) + "</tbody></table>"


def scrapeUnionDay1():
    runnerCount = {
        "S": 0,
        "CP1": 0,
        "CP2": 0,
        "CP3": 0,
        "CP4": 0,
        "G": 0
    }

    srcTable1 = scrape(runnerCount, urlFull1)
    srcTable2 = scrape(runnerCount, urlHalf1)
    return str(srcTable1)+str(srcTable2), runnerCount


def scrapeUnionDay2():
    runnerCount = {
        "S": 0,
        "CP1": 0,
        "CP2": 0,
        "CP3": 0,
        "CP4": 0,
        "G": 0
    }

    srcTable1 = scrape(runnerCount, urlFull2)
    srcTable2 = scrape(runnerCount, urlHalf2)
    return str(srcTable1)+str(srcTable2), runnerCount
