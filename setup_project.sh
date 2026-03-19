#!/bin/bash



folders=(

"00_bootcamp_foundations/python_basics"

"00_bootcamp_foundations/control_structures"

"00_bootcamp_foundations/data_structures"

"00_bootcamp_foundations/file_handling"

"00_bootcamp_foundations/problem_solving"



"01_core_programming/recursion"

"01_core_programming/algorithms"

"01_core_programming/time_complexity"



"02_python_advanced/oops"

"02_python_advanced/decorators"

"02_python_advanced/generators"

"02_python_advanced/context_managers"



"03_data_handling/numpy"

"03_data_handling/pandas"

"03_data_handling/data_cleaning"

"03_data_handling/data_visualization"



"04_machine_learning/supervised_learning"

"04_machine_learning/unsupervised_learning"

"04_machine_learning/feature_engineering"

"04_machine_learning/model_evaluation"



"05_deep_learning/neural_networks"

"05_deep_learning/cnn"

"05_deep_learning/rnn"

"05_deep_learning/pytorch"



"06_nlp/text_processing"

"06_nlp/embeddings"

"06_nlp/transformers"



"07_ai_systems/llms"

"07_ai_systems/prompt_engineering"

"07_ai_systems/rag"

"07_ai_systems/vector_databases"



"08_projects/beginner_projects"

"08_projects/intermediate_projects"

"08_projects/advanced_projects"



"09_mlops_and_deployment/docker"

"09_mlops_and_deployment/api_deployment"

"09_mlops_and_deployment/monitoring"



"assets/datasets"

"assets/images"

)



echo "🚀 Creating AI Mastery Structure..."



for folder in "${folders[@]}"

do

  mkdir -p "$folder"

  touch "$folder/.gitkeep"

done



echo "✅ Done! Structure ready."
