#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
arXiv AI论文爬虫

这个脚本用于自动抓取arXiv上最新的AI相关论文信息，包括标题、作者、摘要和链接。
"""

import json
import requests
import time
from bs4 import BeautifulSoup
import argparse
from datetime import datetime


def fetch_arxiv_page(url):
    """
    获取arXiv页面内容
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"获取页面时出错: {e}")
        return None


def extract_paper_links(html_content):
    """
    从arXiv搜索结果页面提取论文链接
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    paper_links = []
    
    # 查找论文链接
    for entry in soup.select('li.arxiv-result'):
        link_element = entry.select_one('p.title > a')
        if link_element and 'href' in link_element.attrs:
            paper_id = link_element['href'].split('/')[-1]
            paper_links.append({
                'id': paper_id,
                'url': f"https://arxiv.org/abs/{paper_id}"
            })
    
    return paper_links[:10]  # 只返回前10篇论文


def extract_paper_details(html_content):
    """
    从论文详情页面提取论文信息
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 提取论文ID
    paper_id = soup.select_one('meta[name="citation_arxiv_id"]')
    paper_id = paper_id['content'] if paper_id else ''
    
    # 提取标题
    title = soup.select_one('meta[name="citation_title"]')
    title = title['content'] if title else ''
    
    # 提取作者
    authors = []
    author_elements = soup.select('meta[name="citation_author"]')
    for author in author_elements:
        authors.append(author['content'])
    
    # 提取摘要
    abstract = soup.select_one('.abstract')
    abstract = abstract.text.replace('Abstract:', '').strip() if abstract else ''
    
    # 提取日期
    date = soup.select_one('meta[name="citation_date"]')
    date = date['content'] if date else ''
    
    return {
        'id': paper_id,
        'title': title,
        'authors': authors,
        'abstract': abstract,
        'date': date,
        'url': f"https://arxiv.org/abs/{paper_id}"
    }


def save_papers_to_json(papers, output_file):
    """
    将论文信息保存为JSON文件
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)
    print(f"已将{len(papers)}篇论文信息保存到{output_file}")


def generate_markdown(papers, output_file):
    """
    生成Markdown格式的论文列表
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 最新AI研究论文摘要集合\n\n")
        f.write("本仓库收集了来自arXiv的最新AI研究论文摘要，用于跟踪人工智能领域的最新进展。\n\n")
        f.write(f"*最后更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
        f.write("## 论文列表\n\n")
        
        for i, paper in enumerate(papers, 1):
            f.write(f"### {i}. {paper['title']}\n")
            f.write(f"**ID:** {paper['id']}  \n")
            f.write(f"**日期:** {paper['date']}  \n")
            f.write(f"**作者:** {', '.join(paper['authors'])}  \n")
            f.write(f"**摘要:** {paper['abstract']}\n\n")
    
    print(f"已生成Markdown文件: {output_file}")


def main():
    parser = argparse.ArgumentParser(description='抓取arXiv上的AI论文')
    parser.add_argument('--query', type=str, default='cat:cs.AI', help='搜索查询')
    parser.add_argument('--max_papers', type=int, default=10, help='最大论文数量')
    parser.add_argument('--json_output', type=str, default='papers.json', help='JSON输出文件')
    parser.add_argument('--md_output', type=str, default='README.md', help='Markdown输出文件')
    args = parser.parse_args()
    
    # 构建搜索URL
    search_url = f"https://arxiv.org/search/?query={args.query}&searchtype=all&source=header"
    
    # 获取搜索结果页面
    print(f"正在获取搜索结果: {search_url}")
    search_html = fetch_arxiv_page(search_url)
    if not search_html:
        print("无法获取搜索结果页面")
        return
    
    # 提取论文链接
    paper_links = extract_paper_links(search_html)
    print(f"找到{len(paper_links)}篇论文")
    
    # 获取每篇论文的详细信息
    papers = []
    for i, link in enumerate(paper_links[:args.max_papers], 1):
        print(f"正在处理第{i}篇论文: {link['url']}")
        paper_html = fetch_arxiv_page(link['url'])
        if paper_html:
            paper_info = extract_paper_details(paper_html)
            papers.append(paper_info)
            # 添加延迟，避免请求过于频繁
            time.sleep(1)
    
    # 保存为JSON和Markdown
    if papers:
        save_papers_to_json(papers, args.json_output)
        generate_markdown(papers, args.md_output)
        print("爬取完成!")
    else:
        print("未找到任何论文信息")


if __name__ == "__main__":
    main()
