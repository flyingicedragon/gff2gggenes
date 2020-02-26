import gffutils

# 导入 gff 文件，会生成数据库
# gffData = gffutils.create_db('tem.gff', dbfn='tem.db')
# 导入数据库
gffData = gffutils.FeatureDB('tem.db', keep_order=True)
# 初始化列表
gffGene = ['molecule,gene,start,end,strand,direction']
gffSubGene = ['molecule,gene,start,end,strand,subgene,from,to']
# 遍历所有 gene
for i in gffData.all_features(featuretype='gene'):
    if i.strand == '+':
        strand = 'forward'
        direction = '1'
    else:
        strand = 'reverse'
        direction = '-1'
    # 组装 gene 列表字符串并添加
    gffGene.append('tem,' + i['Name'][0] + ',' + str(i.start) + ',' + str(i.end) + ',' + strand + ',' + direction)
    # 遍历 gene 的所有子项，如mRNA等
    for j in gffData.children(i.id):
        # 组装 subgene 列表字符串并添加
        gffSubGene.append('tem,' + i['Name'][0] + ',' + str(i.start) + ',' + str(i.end) + ',' + strand + ',' + j.featuretype + ',' + str(j.start) + ',' + str(j.end))
# 将列表字符串拼接
gffGeneContent = '\n'.join(gffGene)
gffGeneContent += '\n'
gffSubGeneContent = '\n'.join(gffSubGene)
gffSubGeneContent += '\n'
# 导出
temGene = open('temGene.csv', 'w')
temGene.write(gffGeneContent)
temSubGene = open('temSubGene.csv', 'w')
temSubGene.write(gffSubGeneContent)
temGene.close()
temSubGene.close()
