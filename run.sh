#!/bin/zsh

subjects=('abstract_algebra' 'anatomy' 'astronomy' 'business_ethics' 'clinical_knowledge' 'college_biology' 'college_chemistry' 'college_computer_science' 'college_mathematics' 'college_medicine' 'college_physics' 'computer_security' 'conceptual_physics' 'econometrics' 'electrical_engineering' 'elementary_mathematics' 'formal_logic' 'global_facts' 'high_school_biology' 'high_school_chemistry' 'high_school_computer_science' 'high_school_european_history' 'high_school_geography' 'high_school_government_and_politics' 'high_school_macroeconomics' 'high_school_mathematics' 'high_school_microeconomics' 'high_school_physics' 'high_school_psychology' 'high_school_statistics' 'high_school_us_history' 'high_school_world_history' 'human_aging' 'human_sexuality' 'international_law' 'jurisprudence' 'logical_fallacies' 'machine_learning' 'management' 'marketing' 'medical_genetics' 'miscellaneous' 'moral_disputes' 'moral_scenarios' 'nutrition' 'philosophy' 'prehistory' 'professional_accounting' 'professional_law' 'professional_medicine' 'professional_psychology' 'public_relations' 'security_studies' 'sociology' 'us_foreign_policy' 'virology' 'world_religions')

# subjects=('elementary_mathematics' 'formal_logic' 'global_facts' 'high_school_biology' 'high_school_chemistry' 'high_school_computer_science' 'high_school_european_history' 'high_school_geography' 'high_school_government_and_politics' 'high_school_macroeconomics' 'high_school_mathematics' 'high_school_microeconomics' 'high_school_physics' 'high_school_psychology' 'high_school_statistics' 'high_school_us_history' 'high_school_world_history' 'human_aging' 'human_sexuality' 'international_law' 'jurisprudence' 'logical_fallacies' 'machine_learning' 'management' 'marketing' 'medical_genetics' 'miscellaneous' 'moral_disputes' 'moral_scenarios' 'nutrition' 'philosophy' 'prehistory' 'professional_accounting' 'professional_law' 'professional_medicine' 'professional_psychology' 'public_relations' 'security_studies' 'sociology' 'us_foreign_policy' 'virology' 'world_religions')

model="gemma2:27b"

for subject in "${subjects[@]}"
do
    input="data/mmlu_parquet/${subject}.parquet"
    output="data/output/${model}_${subject}_output.csv"

    echo "正在跑$input ..."
    python3 main.py --model "ollama/${model}" --input_file "$input" --score_file "${model}.csv" --language "eng"
done