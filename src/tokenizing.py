from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")

# print(tokenizer.vocab)

token_ids = tokenizer.encode("This is the text that I want to test.")

print(token_ids)
print(tokenizer.convert_ids_to_tokens(token_ids))
