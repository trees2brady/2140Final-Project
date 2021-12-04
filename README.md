# 2140SearchEnging
## Class Project 
1.正常clone远程仓库代码到本地

2.试运行：python manage.py runserver，如缺少相关库则自行安装

3.下载原始数据材料(https://www.trec-cds.org/2021.html)到本地并解压

4.在IndexConstruction\IndexingWithWhoosh\PreProssedCorpusReader.py中修改函数create_path_file中的part_pathx为自己解压的目录

5.运行IndexConstruction\IndexingWithWhoosh\PreProssedCorpusReader.py下的create_path_file函数创建xml_path.txt文件

6.运行IndexConstruction\ConstructIndex.py文件创建index
