# all_in_one_eval

## 簡介

此程式用於評估大型語言模型（LLM）在 繁體中文 + 英文 資料集（多選題）上的表現，並計算模型的得分。程式支透過 litellm API 與指定的模型互動完成評估。

## 範例用法
```python
python3 main.py --model "ollama/llama3.2:3b" --input_file "data.csv" --score_file "output.csv" --language "eng"
```

## 可用參數說明：
| 參數名稱           | 必填   | 預設值                      | 功能說明                                                                 |
|--------------------|--------|----------------------------|------------------------------------------------------------------------|
| `--model`          | 否     | `ollama/llama3.2`          | 指定 LLM 模型名稱，用於 `litellm` API                                    |
| `--input_file`     | 是     | `./data/test.csv`          | 評估資料集的檔案路徑，支援格式：CSV、JSON、PARQUET                        |
| `--response_file`  | 否     | 無                         | 模型回應的保存路徑（若需要保存回應）                                      |
| `--score_file`     | 是     | 無                         | 評估結果（得分）的保存路徑                                              |
| `--language` 或 `--lang` | 否 | `eng`                     | 指定語言，英語輸入用 `'eng'`，中文輸入用 `'chi'`                          |


## 內置Prompt
```python
multiple_choice_prompt_eng = """Please answer the following question by only outputting the letter of the answer (A, B, C, or D). Do not provide any explanations or descriptions:
Question: %s
A) %s
B) %s
C) %s
D) %s
Answer: 
"""


multiple_choice_prompt_chi = """請回答以下問題，只輸出答案的字母（A、B、C或D），不需要其他解釋或描述：
問題: %s
A) %s
B) %s
C) %s
D) %s
答案: 
"""
```

## 目前結果
已在 MMLU 資料集上評估完一些 LLM，簡單結果如下：
|llama3.1:8b|llama3.2:3b|gemma2:27b|
|---|---|---|
|51.37447418|51.28937745|74.44567113|

詳細分數請點此連結[link](https://docs.google.com/spreadsheets/d/1u742QDhFge8NZed17UzMTZgsku4iRoS2ECnA3B5uut4/edit?usp=sharing)