# gff2gggene

## 依赖情况

本工具依赖于 gffutils 包。

## 使用说明

### 安装依赖

使用 `conda` 或者 `pip` 进行安装。

``` powershell
conda install gffutils
pip install gffutils
```

### gff 文件预处理

对 gff 文件进行预处理，截取仅包含所需基因的 gff 内容。建议在 Linux 中使用 `sed` 命令完成。

### 程序调用

Windows 中利用 powershell 调用程序：

``` powershell
python .\gff2gggene.py example.gff
python .\gff2gggene.py example.gff sub
```

Linux 中利用 console 调用程序：

``` shell
python ./gff2gggene.py example.gff
python ./gff2gggene.py example.gff sub
```

根据安装 Python 的版本不同，可能需要将“python”替换为“python3”。

不添加 `sub` 参数，表示将各基因的情况进行输出；添加 `sub` 参数，表示输出各基因子区域（例如：mRNA、CDS等，与 gff 文件内容有关）。

### 结果输出

界面显示“完成”表示程序运行成功。csv 文件输出到工作路径中，文件名结尾是“_Gene.csv”或者“_SubGene.csv”。
