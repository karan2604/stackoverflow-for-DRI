import os
import openai
import argparse

openai.api_type = "azure"
openai.api_base = ""
openai.api_key = ""
openai.api_version = "2024-08-01-preview"

parser = argparse.ArgumentParser()
parser.add_argument('Working_Folder_Path', type=str)
parser.add_argument('ICM_ID', type=int)

args = parser.parse_args()

# Example of a chat completion request
response = openai.ChatCompletion.create(
    engine="",  # Replace with your deployment name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."}
    ]
)


def summarize_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    chunks = [text[i:i + 4000] for i in range(0, len(text), 4000)]

    summaries = []
    for chunk in chunks:
        response = openai.ChatCompletion.create(
            engine="schaudhari21",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Summarize the following text:\n{chunk}"}
            ],
            max_tokens=100
        )
        summaries.append(response['choices'][0]['message']['content'].strip())

    return " ".join(summaries)


input_file_path = f"{args.Working_Folder_Path}\\Information_{args.ICM_ID}.txt"
print(input_file_path)
summary = summarize_text(input_file_path)
print(summary)
output_file_path = f"{args.Working_Folder_Path}\\Summary_{args.ICM_ID}.txt"

with open(output_file_path, 'w') as file:
    file.write(summary + '\n')

# Print the assistant's response
print(response['choices'][0]['message']['content'])