from bs4 import BeautifulSoup
import requests

#미디어랩스 각 학과 교수 이메일 크롤링


#크롤링 된 텍스트를 string 으로 변환하고 슬래시 제거
def change(name):
    name = name[0].text
    name = name.replace("/", "")
    name = str(name)

    return name

#한국문화콘텐츠학과

url = "https://labs.sch.ac.kr/department/kcontents/01.php#department-professorS"

req = requests.get(url)
html= req.text

li = []
soup = BeautifulSoup(html,'html.parser')
junsungwoon = soup.select("#department-professorS > div > div:nth-child(2) > div.profile-contents > h4")
junghyekyung = soup.select("#department-professorS > div > div:nth-child(3) > div.profile-contents > h4")
leejungyeop = soup.select("#department-professorS > div > div:nth-child(4) > div.profile-contents > h4")
leeyoungsoo = soup.select("#department-professorS > div > div:nth-child(5) > div.profile-contents > h4")

li.append(change(junsungwoon))
li.append(change(junghyekyung))
li.append(change(leejungyeop))
li.append(change(leeyoungsoo))


f = open('/ml_email\\kcon_email.txt', 'w', encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()

#영미학과

url = "https://labs.sch.ac.kr/department/eng/01.php#department-professorS"
soup = BeautifulSoup(html,'html.parser')
req = requests.get(url)
html= req.text
li = []

leehyunwoo = soup.select("#department-professorS > div > div:nth-child(2) > div.profile-contents > h4")
parkkipyo = soup.select("#department-professorS > div > div:nth-child(3) > div.profile-contents > h4")
parkjuyoung = soup.select("#department-professorS > div > div:nth-child(4) > div.profile-contents > h4")
choiyoungsik = soup.select("#department-professorS > div > div:nth-child(5) > div.profile-contents > h4")
jinjooyoung = soup.select("#department-professorS > div > div:nth-child(6) > div.profile-contents > h4")
yoonmison = soup.select("#department-professorS > div > div:nth-child(7) > div.profile-contents > h4")
paulcunningham = soup.select("#department-professorS > div > div:nth-child(8) > div.profile-contents > h4")
aronpooley = soup.select("#department-professorS > div > div:nth-child(9) > div.profile-contents > h4")
jpzukauskas = soup.select("#department-professorS > div > div:nth-child(10) > div.profile-contents > h4")


li.append(change(leehyunwoo))
li.append(change(parkkipyo))
li.append(change(parkjuyoung))
li.append(change(choiyoungsik))
li.append(change(jinjooyoung))
li.append(change(yoonmison))
li.append(change(paulcunningham))
li.append(change(aronpooley))
li.append(change(jpzukauskas))


f = open('/ml_email\\eng_email.txt', 'w', encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()

#중국학과

url = "https://labs.sch.ac.kr/department/china/01.php#department-professorS"
soup = BeautifulSoup(html,'html.parser')
req = requests.get(url)
html= req.text
li = []

hongsenggik= soup.select("#department-professorS > div > div:nth-child(2) > div.profile-contents > h4")
parkhyungchun =  soup.select("#department-professorS > div > div:nth-child(3) > div.profile-contents > h4")
imsanghun =  soup.select("#department-professorS > div > div:nth-child(4) > div.profile-contents > h4")
leejongchan =  soup.select("#department-professorS > div > div:nth-child(5) > div.profile-contents > h4")

li.append(change(hongsenggik))
li.append(change(parkhyungchun))
li.append(change(imsanghun))
li.append(change(leejongchan))


f = open('/ml_email\\china_email.txt', 'w', encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()

#미디어커뮤니케이션학과

url = "https://labs.sch.ac.kr/department/media-communication/01.php"
soup = BeautifulSoup(html,'html.parser')
req = requests.get(url)
html= req.text
li = []

janghosoon = soup.select("#department-professorS > div > div:nth-child(2) > div.profile-contents > h4")
yoohyunsuk = soup.select("#department-professorS > div > div:nth-child(3) > div.profile-contents > h4")
simmisun = soup.select("#department-professorS > div > div:nth-child(4) > div.profile-contents > h4")
wonjongwon = soup.select("#department-professorS > div > div:nth-child(5) > div.profile-contents > h4")
jungyoonkyung = soup.select("#department-professorS > div > div:nth-child(6) > div.profile-contents > h4")
hongkyungsoo = soup.select("#department-professorS > div > div:nth-child(7) > div.profile-contents > h4")
choijunhyuk= soup.select("#department-professorS > div > div:nth-child(8) > div.profile-contents > h4")
gigookguan = soup.select("#department-professorS > div > div:nth-child(9) > div.profile-contents > h4")
kimwoochul = soup.select("#department-professorS > div > div:nth-child(10) > div.profile-contents > h4")

li.append(change(janghosoon))
li.append(change(yoohyunsuk))
li.append(change(simmisun))
li.append(change(wonjongwon))
li.append(change(jungyoonkyung))
li.append(change(hongkyungsoo))
li.append(change(choijunhyuk))
li.append(change(gigookguan))
li.append(change(kimwoochul))


f = open('/ml_email\\media_email.txt', 'w', encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()

#건축학과
url = "https://labs.sch.ac.kr/department/architecture/01.php"
soup = BeautifulSoup(html,'html.parser')
req = requests.get(url)
html= req.text
li = []

moonbyungkook = soup.select("#department-professorS > div > div:nth-child(2) > div.profile-contents > h4")
leeyongjae =soup.select("#department-professorS > div > div:nth-child(3) > div.profile-contents > h4")
leeilhyung =soup.select("#department-professorS > div > div:nth-child(4) > div.profile-contents > h4")
leetaehee =soup.select("#department-professorS > div > div:nth-child(5) > div.profile-contents > h4")
parkjongki =soup.select("#department-professorS > div > div:nth-child(6) > div.profile-contents > h4")
imhyunsoo =soup.select("#department-professorS > div > div:nth-child(7) > div.profile-contents > h4")

li.append(change(moonbyungkook))
li.append(change(leeyongjae))
li.append(change(leeilhyung))
li.append(change(leetaehee))
li.append(change(parkjongki))
li.append(change(imhyunsoo))


f = open('/ml_email\\architecture_email.txt', 'w', encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()

#디지털애니메이션학과

url ="https://labs.sch.ac.kr/department/digital_animation/01.php#department-professorS"
soup = BeautifulSoup(html,'html.parser')
req = requests.get(url)
html= req.text
li = []

hongsoongu = soup.select("#department-professorS > div > div:nth-child(2) > div.profile-contents > h4")
kimleejin = soup.select("#department-professorS > div > div:nth-child(3) > div.profile-contents > h4")
kimjungki = soup.select("#department-professorS > div > div:nth-child(4) > div.profile-contents > h4")

li.append(change(hongsoongu))
li.append(change(kimleejin))
li.append(change(kimjungki))

f = open('/ml_email\\ani_email.txt', 'w', encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()

#빅데이터공학과

url = "https://labs.sch.ac.kr/department/bigdata/01.php"
soup = BeautifulSoup(html,'html.parser')
req = requests.get(url)
html= req.text
li = []

chojungki = soup.select("#department-professorS > div > div:nth-child(2) > div.profile-contents > h4")
woojiyoung =soup.select("#department-professorS > div > div:nth-child(3) > div.profile-contents > h4")
jungyoungsup = soup.select("#department-professorS > div > div:nth-child(4) > div.profile-contents > h4")
kimyoungmin =soup.select("#department-professorS > div > div:nth-child(5) > div.profile-contents > h4")
kimjunghyun =soup.select("#department-professorS > div > div:nth-child(6) > div.profile-contents > h4")

li.append(change(chojungki))
li.append(change(woojiyoung))
li.append(change(jungyoungsup))
li.append(change(kimyoungmin))
li.append(change(kimjunghyun))

f = open('/ml_email\\bigdata_email.txt', 'w', encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()

#사물인터넷학과
url = "https://labs.sch.ac.kr/department/iot/01.php"
soup = BeautifulSoup(html,'html.parser')
req = requests.get(url)
html= req.text
li = []

junchangwhan  = soup.select("#department-professorS > div > div:nth-child(2) > div.profile-contents > h4")
yoonjaesuk = soup.select("#department-professorS > div > div:nth-child(3) > div.profile-contents > h4")
kimdaehee  = soup.select("#department-professorS > div > div:nth-child(4) > div.profile-contents > h4")
kimdongmin  = soup.select("#department-professorS > div > div:nth-child(5) > div.profile-contents > h4")
leekyuhang  = soup.select("#department-professorS > div > div:nth-child(6) > div.profile-contents > h4")

li.append(change(junchangwhan))
li.append(change(yoonjaesuk))
li.append(change(kimdaehee))
li.append(change(kimdongmin))
li.append(change(leekyuhang))

f = open('/ml_email\\iot_email.txt', 'w', encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()

#에너지시스템학과
url = "https://labs.sch.ac.kr/department/energy-system/01.php#department-professorS"
soup = BeautifulSoup(html,'html.parser')
req = requests.get(url)
html= req.text
li = []

jungsoonki = soup.select("#department-professorS > div > div:nth-child(2) > div.profile-contents > h4")
chonamchul = soup.select("#department-professorS > div > div:nth-child(3) > div.profile-contents > h4")
anwook = soup.select("#department-professorS > div > div:nth-child(4) > div.profile-contents > h4")
leeyoungwoo= soup.select("#department-professorS > div > div:nth-child(5) > div.profile-contents > h4")
joyonghyun= soup.select("#department-professorS > div > div:nth-child(6) > div.profile-contents > h4")

li.append(change(jungsoonki))
li.append(change(chonamchul))
li.append(change(anwook))
li.append(change(leeyoungwoo))
li.append(change(joyonghyun))


f = open('/ml_email\\energy_email.txt', 'w', encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()

#스마트자동차학과
url = "https://labs.sch.ac.kr/department/smartcar/01.php#department-professorS"
soup = BeautifulSoup(html,'html.parser')
req = requests.get(url)
html= req.text
li = []


kimseungwoo = soup.select("#department-professorS > div > div:nth-child(2) > div.profile-contents > h4")
yanginbum= soup.select("#department-professorS > div > div:nth-child(3) > div.profile-contents > h4")
parksungkeun= soup.select("#department-professorS > div > div:nth-child(4) > div.profile-contents > h4")
songsinhyung= soup.select("#department-professorS > div > div:nth-child(5) > div.profile-contents > h4")
kimtaeyoon= soup.select("#department-professorS > div > div:nth-child(6) > div.profile-contents > h4")

li.append(change(kimseungwoo))
li.append(change(yanginbum))
li.append(change(parksungkeun))
li.append(change(songsinhyung))
li.append(change(kimtaeyoon))

f = open('/ml_email\\smart_email.txt', 'w', encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()

#공연영상학과
url = "https://labs.sch.ac.kr/department/film_theater/01.php#department-professorS"
soup = BeautifulSoup(html,'html.parser')
req = requests.get(url)
html= req.text
li = []

anbyungsoon = soup.select("#department-professorS > div > div:nth-child(2) > div.profile-contents > h4")
minkyungwon= soup.select("#department-professorS > div > div:nth-child(3) > div.profile-contents > h4")
byunjaeran = soup.select("#department-professorS > div > div:nth-child(4) > div.profile-contents > h4")
wonjongwon= soup.select("#department-professorS > div > div:nth-child(5) > div.profile-contents > h4")
kimkyujong= soup.select("#department-professorS > div > div:nth-child(6) > div.profile-contents > h4")
leejinwook= soup.select("#department-professorS > div > div:nth-child(7) > div.profile-contents > h4")

li.append(change(anbyungsoon))
li.append(change(minkyungwon))
li.append(change(byunjaeran))
li.append(change(wonjongwon))
li.append(change(kimkyujong))
li.append(change(leejinwook))

f = open('/ml_email\\performance_email.txt', 'w', encoding='utf-8')
for c in li:
    f.write(c)
    f.write('\n')

f.close()
