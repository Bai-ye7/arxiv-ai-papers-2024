# 使用指南

本文档提供了如何使用本仓库中的工具来抓取和管理arXiv上最新AI研究论文的详细说明。

## 环境准备

1. 确保您已安装Python 3.6或更高版本
2. 安装所需依赖包：

```bash
pip install -r requirements.txt
```

## 使用爬虫脚本

### 基本用法

运行以下命令抓取最新的AI论文：

```bash
python scraper.py
```

这将使用默认参数抓取arXiv上计算机科学人工智能类别（cs.AI）的最新10篇论文，并将结果保存为`papers.json`和`README.md`文件。

### 高级选项

脚本支持以下命令行参数：

- `--query`: 搜索查询，默认为`cat:cs.AI`（计算机科学人工智能类别）
- `--max_papers`: 要抓取的最大论文数量，默认为10
- `--json_output`: JSON输出文件路径，默认为`papers.json`
- `--md_output`: Markdown输出文件路径，默认为`README.md`

例如，要抓取机器学习类别的最新20篇论文：

```bash
python scraper.py --query="cat:cs.LG" --max_papers=20
```

要抓取包含特定关键词的论文：

```bash
python scraper.py --query="all:transformer+AND+cat:cs.AI"
```

## 查询语法

arXiv支持复杂的搜索查询语法，以下是一些常用示例：

- 按类别搜索：`cat:cs.AI`（人工智能）、`cat:cs.LG`（机器学习）、`cat:cs.CL`（计算语言学）
- 按关键词搜索：`all:transformer`、`all:"large language model"`
- 组合搜索：`all:transformer+AND+cat:cs.AI`
- 按作者搜索：`au:"Hinton"`

更多查询语法请参考[arXiv高级搜索帮助](https://arxiv.org/search/advanced)。

## 定期更新

您可以设置定时任务（如cron作业）来定期运行脚本，自动更新仓库中的论文信息。

例如，在Linux系统上，可以添加以下cron作业每天早上8点运行脚本：

```bash
0 8 * * * cd /path/to/repo && python scraper.py
```

## 数据格式

### JSON格式

`papers.json`文件包含以下格式的论文信息：

```json
[
  {
    "id": "论文ID",
    "title": "论文标题",
    "authors": ["作者1", "作者2", ...],
    "abstract": "论文摘要",
    "date": "发布日期",
    "url": "论文URL"
  },
  ...
]
```

### Markdown格式

`README.md`文件以易于阅读的格式展示论文信息，包括标题、作者、日期和摘要。

## 贡献

欢迎通过Pull Request贡献代码或提出改进建议。如果您发现任何问题，请创建Issue。

## 许可证

本项目采用MIT许可证。详情请参阅LICENSE文件。