from afinn import Afinn

afinn = Afinn()

pos_file = open("./pos_30.txt","r")
pos_line = pos_file.readlines()


line_list = []

for oneline in pos_line:
    if "\n" in oneline:
        oneline.rstrip("\n")
        line_list.append(oneline)

score_list = []
pos_file.close()
pos_list = []
pos_result = open("pos_result_str.txt", "w")

for line1 in line_list:
   result = afinn.score(line1)
   result = str(result)
   pos_line = str(pos_result.writelines(line1))
   pos_score = str(pos_result.writelines(result))
   form = pos_line+","+ pos_score






pos_result.close()

pos_list.append(form)
# pos_file.close()
print(pos_list[0])

# 구분자는 , comma