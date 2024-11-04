import pandas as pd
import json

def load_file(input_file):
    if input_file.endswith(".csv"):
        data = pd.read_csv(input_file)
    elif input_file.endswith(".json"):
        with open(input_file, "r", encoding="utf-8") as f:
            data = pd.DataFrame(json.load(f))
    else:
        raise ValueError("Unsupported file format. Use CSV or JSON.")
    return data

def get_multi_csv(file_path):
    df = pd.read_csv(file_path)
    
    questions = df["question"].tolist()
    choices_A = df["A"].tolist()
    choices_B = df["B"].tolist()
    choices_C = df["C"].tolist()
    choices_D = df["D"].tolist()
    answers = df["answer"].tolist()
    
    return questions, choices_A, choices_B, choices_C, choices_D, answers


def get_multi_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    questions = [item["question"] for item in data]
    choices_A = [item["A"] for item in data]
    choices_B = [item["B"] for item in data]
    choices_C = [item["C"] for item in data]
    choices_D = [item["D"] for item in data]
    answers = [item["answer"] for item in data]
    
    return questions, choices_A, choices_B, choices_C, choices_D, answers