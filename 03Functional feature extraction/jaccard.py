import csv

interaction_dict = {}
with open('../../../dataset/755/interaction.csv', 'r') as interaction_file:
    csv_reader = csv.reader(interaction_file)
    for row in csv_reader:
        if len(row) == 2:
            circRNA, miRNA = row
            interaction_dict[(circRNA, miRNA)] = 1

with open('../../../dataset/755/final_circRNA_ID.csv') as circRNA_file:
    circRNA_ids = [line.strip() for line in circRNA_file]

with open('../../../dataset/755/final_miRNA_ID.csv') as miRNA_file:
    miRNA_ids = [line.strip() for line in miRNA_file]

matrix_size = len(circRNA_ids) + len(miRNA_ids)
matrix = [[0] * matrix_size for _ in range(matrix_size)]

each_circRNA_correctioned_miRNAs = {}
for item in circRNA_ids:
    value = set()
    item = item.strip('\n')
    for circRNA, miRNA in interaction_dict:
        if item == circRNA:
            value.add(miRNA)
    each_circRNA_correctioned_miRNAs[item] = list(value)

for i, key1 in enumerate(circRNA_ids):
    for j, key2 in enumerate(circRNA_ids):
        tem = []
        for item in each_circRNA_correctioned_miRNAs[key1]:
            if item in each_circRNA_correctioned_miRNAs[key2]:
                tem.append(item)
        jiao_ji = len(tem)
        bing_ji = len(each_circRNA_correctioned_miRNAs[key1]) + len(each_circRNA_correctioned_miRNAs[key2]) - jiao_ji
        if bing_ji != 0:
            jaccard_similarity = jiao_ji / bing_ji
            matrix[i][j] = jaccard_similarity

each_miRNA_correctioned_circRNAs = {}
for item in miRNA_ids:
    value = set()
    item = item.strip('\n')
    for circRNA, miRNA in interaction_dict:
        if item == miRNA:
            value.add(circRNA)
    each_miRNA_correctioned_circRNAs[item] = list(value)
for i, key1 in enumerate(miRNA_ids):
    for j, key2 in enumerate(miRNA_ids):
        tem = []
        for item in each_miRNA_correctioned_circRNAs[key1]:
            if item in each_miRNA_correctioned_circRNAs[key2]:
                tem.append(item)
        jiao_ji = len(tem)
        bing_ji = len(each_miRNA_correctioned_circRNAs[key1]) + len(each_miRNA_correctioned_circRNAs[key2]) - jiao_ji
        if bing_ji != 0:
            jaccard_similarity = jiao_ji / bing_ji
            matrix[i + len(circRNA_ids)][j + len(circRNA_ids)] = jaccard_similarity

for j, circRNA in enumerate(circRNA_ids):
    for i, miRNA in enumerate(miRNA_ids):
        if (circRNA, miRNA) in interaction_dict:
            matrix[i + len(circRNA_ids)][j] = 1
            matrix[j][i + len(circRNA_ids)] = 1

header = circRNA_ids + miRNA_ids


with open('Jaccard_matrix.csv', 'w', newline='') as transposed_file:
    csv_writer = csv.writer(transposed_file)



