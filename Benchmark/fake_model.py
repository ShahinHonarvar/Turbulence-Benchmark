from helper_functions import instantiate
import json


response_template = {
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "content": "",
                "role": "assistant"
            }
        }
    ],
    "created": 1684019121,
    "id": "chatcmpl-7Fsaf22rduSunNZhRaMmFE7JTtCzE",
    "model": "gpt-3.5-turbo-0301",
    "object": "chat.completion",
    "usage": {
        "completion_tokens": 20,
        "prompt_tokens": 90,
        "total_tokens": 110
    }
}

def run_model(q_no, c, model, params, text, no):
    with open(f'Q{q_no}/solution.py.template', 'r') as f, open(f'Q{q_no}/{model}_results_{no}/Folder_{c}/response.json', 'w') as f1:
        solution_template = f.read()
        solution = instantiate(solution_template, params)
        response_template["choices"][0]["message"]["content"] = "```" + str(solution) + "```"
        json.dump(response_template, f1, ensure_ascii=False, indent=2)
        prompt = f"Here is a text specification delimited by angle brackets. Create Python code according to the text specification. The Python code should not contain any comments. The Python code should be delimited only by triple backticks. <{text}>"
    
    return prompt
        
