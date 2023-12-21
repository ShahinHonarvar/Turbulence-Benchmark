import os
import cohere

API_KEY = os.getenv('COHERE_KEY')
co = cohere.Client(API_KEY)


def get_code(model_params, prompt):
    response = co.generate(
        prompt=prompt,

        # command-xlarge-beta, command-medium-beta, command-medium-nightly, medium, xlarge, command-xlarge-nightly
        # command, command-nightly, command-light-nightly, command-light
        model=model_params['model'],

        # Can only be set to 0 if return_likelihoods is set to ALL to get the likelihood of the prompt.
        max_tokens=model_params['max_tokens'],

        # Defaults to 0.75, min value of 0.0, max value of 5.0. A non-negative float that tunes the degree of
        # randomness in generation. Lower temperatures mean less random generations.
        temperature=model_params['temperature'],

        # Defaults to 1, min value of 1, max value of 5. Denotes the maximum number of generations that
        # will be returned.
        # num_generations=1,

        # Defaults to 0(disabled), which is the minimum. Maximum value is 500. Ensures only the top k most likely
        # tokens are considered for generation at each step.
        # k=0,

        # Defaults to 0.75. Set to 1.0 or 0 to disable. If set to a probability 0.0 < p < 1.0, it ensures that
        # only the most likely tokens, with total probability mass of p, are considered for generation at each step.
        # If both k and p are enabled, p acts after k.
        # p=p,

        # Defaults to 0.0, min value of 0.0, max value of 1.0. Can be used to reduce repetitiveness of generated tokens.
        # The higher the value, the stronger a penalty is applied to previously present tokens, proportional to
        # how many times they have already appeared in the prompt or prior generation.
        frequency_penalty=model_params['frequency_penalty'],

        # Defaults to 0.0, min value of 0.0, max value of 1.0. Can be used to reduce repetitiveness of generated tokens.
        # Similar to frequency_penalty, except that this penalty is applied equally to all tokens that have already
        # appeared, regardless of their exact frequencies.
        presence_penalty=model_params['presence_penalty'],

        # The generated text will be cut at the beginning of the earliest occurrence of an end sequence.
        # The sequence will be excluded from the text.
        # end_sequences='',

        # The generated text will be cut at the end of the earliest occurrence of a stop sequence.
        # The sequence will be included the text.
        # stop_sequences=["--"],

        # One of GENERATION|ALL|NONE to specify how and if the token likelihoods are returned with the response.
        # Defaults to NONE.
        # If GENERATION is selected, the token likelihoods will only be provided for generated text.
        # If ALL is selected, the token likelihoods will be provided both for the prompt and the generated text.
        # return_likelihoods=None,

        # Used to prevent the model from generating unwanted tokens or to incentivize it to include desired tokens.
        # The format is {token_id: bias} where bias is a float between -10 and 10. Tokens can be obtained from text
        # using Tokenize.
        # For example, if the value {'11': -10} is provided, the model will be very unlikely to include the token 11
        # ("\n", the newline character) anywhere in the generated text. In contrast, {'11': 10} will result in
        # generations that nearly only contain that token. Values between -10 and 10 will proportionally affect the
        # likelihood of the token appearing in the generated text.
        # Note: logit bias may not be supported for all custom models.
        # logit_bias={},

        # One of NONE|START|END to specify how the API will handle inputs longer than the maximum token length.
        # Passing START will discard the start of the input. END will discard the end of the input. In both cases,
        # input is discarded until the remaining input is exactly the maximum input token length for the model.
        # If NONE is selected, when the input exceeds the maximum input token length an error will be returned.
        # truncate=None
    )

    return response


def run_cohere_model(model_params, text):

    prompt = f'Here is a text specification delimited by angle brackets. Create Python code according to the text specification. The Python code should not contain any comments. The Python code should be delimited only by triple backticks. <{text}>'
    response = get_code(model_params, prompt)

    return response, prompt
