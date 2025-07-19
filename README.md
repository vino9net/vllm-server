
## run test program
create a ```.env``` with HuggingFace token

```text
HF_TOKEN="hf_xxx"
HUGGINGFACE_HUB_TOKEN="hf_xxx"
```

```shell
# the following will download the model
# and run inference

uv sync
source .venv/bin/activate
python main.py

```

Run OpenAI API server

```shell
uv sync
source .venv/bin/activate

vllm serve meta-llama/Llama-3.1-8B-Instruct \
  --gpu-memory-utilization 0.95 \
  --max-model-len 2048 \
  --dtype auto \
  --api-key token-abc123

# in a separate terminal
python client.py

```



