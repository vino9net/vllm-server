#!/bin/bash

API_KEY=$(cat .api_key.txt)

vllm serve microsoft/Phi-4-mini-instruct \
  --gpu-memory-utilization 0.9 \
  --max-model-len 4096 \
  --max-num-seqs 128 \
  --max-num-batched-tokens 32768 \
  --enable-chunked-prefill \
  --worker-use-ray \
  --dtype bfloat16 \
  --host 0.0.0.0 \
  --port 8000 \
  --api-key $API_KEY
