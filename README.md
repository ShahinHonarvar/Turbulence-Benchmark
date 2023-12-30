[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/turbulence-systematically-and-automatically/code-generation-on-turbulence)](https://paperswithcode.com/sota/code-generation-on-turbulence?p=turbulence-systematically-and-automatically)

# Turbulence Benchmark

Turbulence is a new benchmark for systematically evaluating the correctness and robustness of instruction-tuned large language models (LLMs) for code generation. Turbulence consists of a large set of natural language question templates, each of which is a programming problem, parameterised so that it can be asked in many different forms. Each question template has an associated test oracle that judges whether a code solution returned by an LLM is correct. Thus, from a single question template, it is possible to ask an LLM a neighbourhood of very similar programming questions, and assess the correctness of the result returned for each question. This new benchmark systematically and automatically identifies cases where LLMs are able to solve some problems in a neighbourhood but do not manage to generalise to solve the whole neighbourhood. Therefore, this method is effective at highlighting robustness issues.

# Turbulence Execution Instructions

To execute the benchmark, please ensure that your operating system is either Linux or macOS and the version of Python installed is at least 3.10. Follow the steps below in the specified order:

## Step 1: Install Required Libraries

Open the terminal and use the `cd` command to move into the Turbulence folder. Use the following command to install all required packages of Python:

`pip install -r requirements.txt`

## Step 2: Set API Keys as Environmental Variables

Configure the OpenAI and Cohere API keys as environmental variables on your operating system. Name the variable for the OpenAI API key as "OPENAI_KEY" and the variable for the Cohere API key as "COHERE_KEY". If you are running a local LLM, then there is no need to configure any key.

## Step 3: Define Prerequisite Settings

Download the `Source_Code` folder. In the `config.json` file, define the prerequisite settings as outlined below:

- Set the "task" to "call_llm" for sending questions to the Large Language Model (LLM) and retrieving generated responses. To test the generated responses, set the "task" to "test".
   
- Specify the model under evaluation and its parameters in the "model_specifications" section.

- Determine the seed value for result replication.

- Indicate the range of questions to send to the LLM and test the corresponding responses. For instance, "1-60" covers questions from 1 to 60 (inclusive). Each question is accompanied by the number of instances. Specify whether the list of generated parameter values should be shuffled using the 'shuffle' attribute. Additionally, determine if fuzzy testing should be done and if yes then specify the number of random inputs for the randomized test phase. Some LLM-generated code may have very lengthy runtime or substantial memory usage. Select the maximum allowable runtime in seconds and specify how much memory should be available.

- Set the "number_of_rounds" to specify the number of experiments. For example, using "1-5" will evaluate the results of all five experiments.

- Provide the absolute path of the folder as the value for the "path" attribute.

## Step 4: Execution
Make sure you are in the folder. Next, enter the command `python3 main.py` and press the enter key to execute it.

---

## Organization of Result Folders and Files in This Repository

In addition to the `Source_Code` folder, there are ten folders, each serving a specific LLM. For instance, `GPT3_5_T_0` consists of the results for _GPT3.5_ with a temperature setting of 0, while `Command_T_D` contains the results for the _Command_ model with the default temperature. Each of these primary folders contains 60 subfolders and four result JSON files: `CCScore.json`, `Classified_CCScores.json`, `difficulty_stat.json`, and `failure_reasons_classes.json`. The data within these files is presented in the corresponding parts of the tables and figures in our paper. 

Within each subfolder labelled `Q<n>` (where *n* is a question number between 1 and 60), there are five subfolders and multiple files. The pair of (question template, test oracle) for each question is available here. The `question.txt.template` file contains the question in English. `genparams.py` contains a function for generating unique random parameter values to replace placeholders in the template. With some questions, we manually wrote 20 parameter values representing the edge cases, and the remaining 80 were generated using the mentioned file. The `test.py.template` file is a template with manually written test cases, and `solution.py.template` is the corresponding model solution template. These template files contain placeholders denoted by enumerated `$`, replaced by corresponding values when instantiated by Turbulence, resulting in question and oracle instances. The `gen_function_params.py` file generates fuzzy inputs for testing the generated function by the LLM. Files starting with `Final_report` are HTML test reports displaying testing information, the number of correct and incorrect responses in each of the five rounds, and the links to the corresponding reports. 

Each question instance was given to the LLM five times. Subfolders named after the LLM, ending with `result_<number>` (1 <= number <= 5), contain rounds of experiments, each with 100 folders and various files such as `all_params.txt` file that holds all parameter values generated by `genparams.py`. Other files include reports, for example, on parameter values to which the LLM generated correct (`correct_params.html`) or incorrect (`wrong_params.html`) answers. Folders labelled `Folder_<folder_number>` (1 <= folder_number <= 100) contain multiple files, including necessary files to run the test and reports like `pre_existing_test_case_report.json` and `fuzzy_test_report.txt`. The `model_specs_prompt.json` file contains the LLM configuration, the question instance, and the complete prompt sent to the LLM. `solution.py` is the instantiated model solution template with corresponding parameter values. `response.json` or `response.txt` contains the entire response returned by the LLM, and if the generated code was parsable, `generated_answer.py` was produced by Turbulence. Other files in these folders are additional test reports.
