from vllm import LLM, SamplingParams
from dotenv import load_dotenv
import os

load_dotenv()

print(f"TOKEN={os.environ['HF_TOKEN']}")

#llm = LLM(model="facebook/opt-125m")

# Initialize model (should fit comfortably in 23GB)
llm = LLM(model='meta-llama/Llama-3.1-8B-Instruct', 
          gpu_memory_utilization=0.9,
          max_model_len=4096)

# Test inference
prompts = ['Analyze this SEC filing text: ...']
sampling_params = SamplingParams(temperature=0.1, max_tokens=256)
outputs = llm.generate(prompts, sampling_params)
print(outputs)
