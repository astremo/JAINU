# import torch
# from transformers import T5ForConditionalGeneration, T5Tokenizer
import os
import requests


class jainu():

    # Using Huggingface Accelerated Inference API

    API_TOKEN = os.environ["ACCESS_TOKEN"]

    API_URL = "https://api-inference.huggingface.co/models/astremo/JAINU"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    t_output = []

    def query(self, payload):
        response = requests.post(self.API_URL, headers=self.headers, json=payload)
        return response.json()

    def request_query(self, text:str):
        self.t_output = self.query({"inputs": f"{text}", "options":{"wait_for_model": True}, "parameters": {"max_length": 128}})
        return self.t_output

    def translate(self, text:str):
        self.request_query(text)
        while ("error" in self.t_output):
            self.request_query(text)
        return self.t_output[0].get("generated_text")

    # Exceeds heroku runtime memory

    # tokenizer = T5Tokenizer.from_pretrained("sonoisa/t5-base-japanese")
    # model = T5ForConditionalGeneration.from_pretrained("astremo/JAINU")

    # def translate(self, text: str):
    #     device = torch.device("cpu")
    #     tokenizer = self.tokenizer
    #     model = self.model
    #     model.to(device)
    #     model.eval()
    #     input_ids = tokenizer.encode(text, max_length=128, padding='max_length', truncation=True, return_tensors="pt")
    #     inputs = input_ids.to(device)
    #     outputs = model.generate(inputs, max_length=128, num_beams=4)
    #     t_output = tokenizer.decode(outputs.cpu().numpy()[0], skip_special_tokens=True)
    #     return t_output
