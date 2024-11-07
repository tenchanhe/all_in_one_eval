import pandas as pd
import argparse
import json
from tqdm import tqdm

from utils import get_multi_csv, get_multi_json, get_multi_pq, output_score
from eval import get_response, get_score, clean_response

# 設定參數
parser = argparse.ArgumentParser(description="Evaluate LLM on Traditional Chinese + English datasets using litellm")
parser.add_argument("--model", type=str, default="ollama/llama3.2", help="Model name for litellm API")
parser.add_argument("--input_file", type=str, default="./data/test.csv", help="Evaluation dataset file path (supports CSV, JSON, PARQUET)")
parser.add_argument("--input_dir", type=str, help="Evaluation dataset file path (supports CSV, JSON)")
parser.add_argument("--output_file", type=str, default='./output.csv', help="Path to save evaluation results")
parser.add_argument("--language", "--lang", required=False, type=str, default='eng', help="english input 'eng', chinese iniput 'chi'")
args = parser.parse_args()


if __name__ == "__main__":
    if (args.input_file).endswith(".csv"):
        questions, A, B, C, D, answers = get_multi_csv(args.input_file)
    elif (args.input_file).endswith(".json"):
        questions, A, B, C, D, answers = get_multi_json(args.input_file)
    elif (args.input_file).endswith(".parquet"):
        questions, A, B, C, D, answers = get_multi_pq(args.input_file)
    else:
        raise ValueError('Not support format')

    # print(answers)
    ori_result=[]
    result = []
    for i in range(len(questions)):
        response = get_response(questions[i], A[i], B[i], C[i], D[i], args.model, args.language)
        # result.append(response['content'])
        cl_response = clean_response(response['choices'][0]['message']['content'])
        print("****", cl_response)

        result.append(cl_response)
        ori_result.append(response['choices'][0]['message']['content'])
        
    score = get_score(result, answers)
    output_score(score, result, ori_result, answers, args.output_file)
    # print('score = ', score)
