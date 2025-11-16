- [ ] **Skeleton Project**
    - [x] Initialize FastAPI app (`main.py`) with a health check endpoint.
    - [ ] Configure environment variables for your platform API key and both provider API keys (Cerebras and MorphLLM) in a `.env` file and `config.py`.

- [ ] **Implement API Key Auth**
    - [ ] Write middleware or a dependency to check incoming requests for your single platform API key.
    - [ ] Reject unauthorized requests immediately.

- [ ] **Create Provider Adapters**
    - [ ] Build simple Python functions or classes in `providers.py` to call Cerebras and MorphLLM APIs using their respective API keys.
    - [ ] Each adapter should have a unified interface.

- [ ] **Implement Unified Route**
    - [ ] In `routes.py`, create one POST route (e.g., `/v1/infer`) that accepts a request with a `model` or `provider` field indicating which backend to call.
    - [ ] Route the request internally via the appropriate function in `providers.py`.
    - [ ] Return the provider's response as-is or in a normalized common format.

- [ ] **Test Locally**
    - [ ] Write simple tests ensuring authentication works, that Cerebras and MorphLLM calls succeed, and that routing logic dispatches correctly.