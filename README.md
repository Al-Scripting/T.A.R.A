# 🧠 T.A.R.A. - Therapeutic AI for Reassurance and Assistance

This document breaks down the CSM (Conversational Speech Model) codebase used for voice generation in T.A.R.A., designed for therapeutic conversational AI.

---

## 📁 File Structure Overview

```
csm/
├── generator.py          # Main generation logic using LLaMA + Mimi
├── models.py             # Model definition and architecture
├── run_csm.py            # Entry point script to generate conversations
├── torch_patch.py        # Monkeypatch to disable torch.compile issues
├── requirements.txt      # Python dependencies
├── prompts/              # Speaker audio samples (downloaded)
└── ...                   # Additional assets/utilities
```

---

## 🧩 File Descriptions

### `run_csm.py`
**Purpose:** Main script that prepares and generates a sample dialogue.

- Imports speaker prompts (text + audio)
- Defines a sample conversation with speakers
- Calls `generator.generate(...)` for each line
- Saves output to `audio.wav`

Key Sections:
```python
prompt_a = prepare_prompt(...)
prompt_b = prepare_prompt(...)
audio = generator.generate(...)
torchaudio.save("audio.wav", audio, ...)
```

---

### `generator.py`
**Purpose:** Handles all interaction with the model.

- Loads CSM-1B with `load_csm_1b(device)`
- Defines the `Segment` class to hold context (text, speaker, audio)
- Generates audio from text using model + speaker context

Key Functions:
```python
def load_csm_1b(device): ...
def prepare_prompt(...): ...
class Segment: ...
```

---

### `models.py`
**Purpose:** Loads and builds the CSM model (LLaMA backbone + Mimi decoder)

- Uses `torchtune` to load LLaMA-3.2-1B
- Integrates Mimi decoder to generate RVQ codes
- Exposes `Model.generate()` for inference

Key Class:
```python
class Model:
    def __init__(...): ...
    def generate(...): ...
```

---

### `torch_patch.py`
**Purpose:** Monkeypatch that disables `torch.compile()` to avoid Windows errors.

```python
import torch

def dummy_compile(fn=None, **kwargs):
    return fn

torch.compile = dummy_compile
```

This ensures stability on Windows and avoids TorchInductor-related crashes.

---

### `prompts/`
**Purpose:** Holds downloaded `.wav` files used as speaker identity references.
- `conversational_a.wav`
- `conversational_b.wav`

These shape the tone and vocal identity of each generated speaker.

---

## 🔄 Inference Flow

```text
1. Load speaker samples and model
2. Wrap previous audio + text as Segments (context)
3. Run generator.generate() with context and new text
4. Return generated audio tensor
5. Save as .wav file
```

---

## 🔧 Customizable Elements

| Element | Customization |
|--------|----------------|
| Voice | Replace `conversational_a/b.wav` with custom samples |
| Text | Change conversation text in `run_csm.py` |
| Model | Swap in fine-tuned variants if available |
| Emotions | Add tone modifiers in text: e.g. "(gently) I’m here for you." |
| Integration | Combine with LLMs (GPT, Claude, etc.) for back-and-forth dialog |

---

Let me know if you'd like a visual diagram or code annotations next. T.A.R.A.'s voice is just getting started. 🎙️