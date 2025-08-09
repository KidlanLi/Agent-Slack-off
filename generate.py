#!/usr/bin/env python3
import json
import os

# Read the JSON data
with open('old/DeepREJECT_small.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Categories for better organization
categories = {
    "Illegal goods and services": "Illegal Goods & Services",
    "Hate, harassment and discrimination": "Hate & Discrimination", 
    "Non-violent crimes": "Non-Violent Crimes",
    "Disinformation and Deception": "Disinformation & Deception",
    "Violence": "Violence",
    "Sexual content": "Sexual Content"
}

# Generate HTML files for talks 1-60
for i, item in enumerate(data, 1):  # Start from index 0 (talk #1)
    prompt = item['forbidden_prompt']
    category = categories.get(item['category'], item['category'])
    
    # Create a title based on the prompt
    title_words = prompt.split()[:5]
    title = " ".join(title_words) + "..."
    
    # 只保留纯文本内容，不包含任何HTML标签
    text_content = f'''Talk #{i}: {prompt}

Discussion Question:
"{prompt}"
'''
    
    # Write the text file (使用.txt扩展名而不是.html)
    with open(f'{i}.txt', 'w', encoding='utf-8') as f:
        f.write(text_content)

# print("Generated 59 text files (2.txt through 60.txt)") 