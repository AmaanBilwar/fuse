## Implementation  
This should be a proxy first approach, users use my platform (or SDK?), provide their api keys and with our one api key, should be able to validate and use any LLMs within our scope with their apps.

> NOTE: LLMs for now, more integrations later that require api keys

## What to Code First:

1. **main.py**  
   - Instantiate FastAPI
   - Include authentication dependency or middleware

2. **config.py**  
   - Securely load your API keys (platform + provider keys)

3. **auth.py**  
   - Implement simple API key check (dependency or middleware)

4. **providers.py**  
   - Define:
     - `call_cerebras(prompt: str)`
     - `call_morphllm(prompt: str)`

5. **models.py**  
   - Minimal Pydantic model for request validation:
     - Fields: `model`, `prompt`

6. **routes.py**  
   - Single `/v1/infer` POST route
   - Accepts JSON: `{ "model": "cerebras" | "morphllm", "prompt": "..." }`
   - Routes request to appropriate provider function
