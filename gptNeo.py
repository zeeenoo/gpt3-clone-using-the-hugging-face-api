
#pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
#pip install transformers
from transformers import pipeline



generator = pipeline('text-generation',model='EleutherAI/gpt-neo-2.7B')
#here we used the hugging face pipeline 


prompt = input('enter the question')
length = int(input('enter the length of the text u want'))
res = generator(prompt,max_length=length,do_sample=True,temperature= 0.9)

#here you find the output 
print(res[0]['generated text'])