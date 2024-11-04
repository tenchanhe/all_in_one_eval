import pandas as pd
import argparse
import json
from tqdm import tqdm

from get_data import load_file, get_multi_csv, get_multi_json
from eval import run_llm, eval

# 設定參數
parser = argparse.ArgumentParser(description="Evaluate LLM on Traditional Chinese + English datasets using litellm")
parser.add_argument("--model", type=str, default="ollama/llama3.2", help="Model name for litellm API")
parser.add_argument("--input_file", type=str, default="./data/test.csv", help="Evaluation dataset file path (supports CSV, JSON)")
parser.add_argument("--input_dir", type=str, help="Evaluation dataset file path (supports CSV, JSON)")
parser.add_argument("--output_file", type=str, default='./output.csv', help="Path to save evaluation results")
parser.add_argument("--language", "--lang", required=False, type=str, default='eng', help="english input 'eng', chinese iniput 'chi'")
args = parser.parse_args()


if __name__ == "__main__":
    if (args.input_file).endswith(".csv"):
        questions, A, B, C, D, answers = get_multi_csv(args.input_file)
    elif (args.input_file).endswith(".json"):
        questions, A, B, C, D, answers = get_multi_json(args.input_file)
    elif args.input_dir:
        i = 1

    # print(questions)
    result = []
    for i in range(len(questions)):
        response = eval(questions[i], A[i], B[i], C[i], D[i], args.model, args.language)
        # result.append(response['content'])
        print("****", response['choices'][0]['message']['content'])
