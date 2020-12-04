from afinn import Afinn

#Afinn 패키지를 사용하면 바로 점수도 나오는듯 하지만 시간이 엄청 오래 걸린다 .
#https://github.com/fnielsen/afinn

afinn = Afinn()

pos_file = open("pos.txt", "r")
pos_line = pos_file.readlines()
score = []

for x in pos_line:
    result = afinn.score(x)
    score.append(result)
pos_file.close()

# 구분자는 , comma

pos_result = open("pos_result.txt", "w")

for x in pos_line:
    for y in score:
        t = pos_result.writelines(x)
        y = str(y)
        str(pos_result.write(y), ",")

pos_result.close()


