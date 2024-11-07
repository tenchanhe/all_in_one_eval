import pandas as pd
import json
import ast


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

    if "choices" in df.columns:
        questions = df["question"].tolist()
        answers = []
        choices_A, choices_B, choices_C, choices_D = [], [], [], []
        num_to_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

        for index, row in df.iterrows():
            # 將 choices 字串轉換為列表
            # parsed_choices = ast.literal_eval(row["choices"])
            # print(row["choices"])
            # 將每個選項分別加入對應的列表
            choices_A.append(row["choices"][0])
            choices_B.append(row["choices"][1])
            choices_C.append(row["choices"][2])
            choices_D.append(row["choices"][3])

            # 將 answer 數字轉換為字母
            answer_index = int(row["answer"])
            answers.append(num_to_letter.get(answer_index, None))

    else:
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

def get_multi_pq(file_path):
    df = pd.read_parquet(file_path)

    if "choices" in df.columns:
        questions = df["question"].tolist()
        answers = []
        choices_A, choices_B, choices_C, choices_D = [], [], [], []
        num_to_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

        for index, row in df.iterrows():
            # 將 choices 字串轉換為列表
            # parsed_choices = ast.literal_eval(row["choices"])
            # print(row["choices"])
            # 將每個選項分別加入對應的列表
            choices_A.append(row["choices"][0])
            choices_B.append(row["choices"][1])
            choices_C.append(row["choices"][2])
            choices_D.append(row["choices"][3])

            # 將 answer 數字轉換為字母
            answer_index = int(row["answer"])
            answers.append(num_to_letter.get(answer_index, None))

    else:
        questions = df["question"].tolist()
        choices_A = df["A"].tolist()
        choices_B = df["B"].tolist()
        choices_C = df["C"].tolist()
        choices_D = df["D"].tolist()
        answers = df["answer"].tolist()
    
    return questions, choices_A, choices_B, choices_C, choices_D, answers



def output_score(score, result, ori_result, answer, output_file):
     # 創建一個 DataFrame，包含 score、result 和 answer
    data = {
        "Result": result,
        "Answer": answer,
        "Ori_response": ori_result
    }
    
    # 將 score 放在 DataFrame 的最上方
    with open(output_file, 'w') as file:
        file.write(f"Score,{score}\n")  # 寫入 score 作為第一行
        pd.DataFrame(data).to_csv(file, index=False)  # 寫入 result 和 answer 從第二行開始
