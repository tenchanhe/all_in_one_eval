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
        # api_base="http://localhost:11434"
    )

    return response


def eval(questions, A, B, C, D, model, lang):
    prompt = get_prompt(questions, A, B, C, D, lang)
    response = run_llm(prompt, model)
    return response