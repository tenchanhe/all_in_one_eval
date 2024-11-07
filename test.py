import re

def clean_response(response):
    match = re.search(r"\b[A-D]\b", response, re.IGNORECASE)
    if match:
        return match.group(0).upper()  # 提取出字母並轉為大寫
    else:
        return response
    
print(clean_response("B)"))