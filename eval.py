import re
from litellm import completion
from prompt_list import *

def get_prompt(questions, A, B, C, D, lang):
    if lang == 'eng':
        prompt = multiple_choice_prompt_eng % (questions, A, B, C, D)
    elif lang == 'chi':
        prompt = multiple_choice_prompt_chi % (questions, A, B, C, D)
    return prompt


def run_llm(prompt, model):
    response = completion(
        model=model,
        messages=[{ "content": prompt, "role": "user"}], 
        temperature=0.1
        # api_base="http://localhost:11434"
    )

    return response


def get_response(questions, A, B, C, D, model, lang):
    prompt = get_prompt(questions, A, B, C, D, lang)
    print(prompt)
    response = run_llm(prompt, model)
    return response


def clean_response(response):
    match = re.search(r"\b[A-D]\b", response, re.IGNORECASE)
    if match:
        return match.group(0).upper()  # 提取出字母並轉為大寫
    else:
        return response


def get_score(result, answer):
    hit = 0
    if len(result) != len(answer):
        raise ValueError('length error')
    else:
        for i in range(len(result)):
            if result[i] == answer[i]:
                hit += 1

    return hit*100/len(result)
