# MOFReasoner

MOFReasoner (currently released as **ChemReasoner**) is a **domain-specific reasoning large language model (LLM)** designed to think like a scientist. It integrates **Chain-of-Thought (CoT) reasoning** and **knowledge distillation** to enhance scientific reasoning in chemistry, with a particular focus on **Metal-Organic Frameworks (MOFs)** adsorption research.

---

## 🚀 Introduction

General-purpose large language models (LLMs) have shown impressive capabilities in natural language understanding and reasoning. However, their lack of domain specialization limits their ability to perform **multi-step scientific reasoning**.  
MOFReasoner addresses this limitation by incorporating domain-specific knowledge, scientific reasoning strategies, and structured CoT reasoning.

Key innovations:

- **Domain Knowledge Integration**: Leveraging over **8,200 research articles** and **500 review papers** to construct a domain-specific CoT dataset.

- **Knowledge Distillation**: Transferring expertise from large teacher models (e.g., DeepSeek-V3, Qwen-Turbo, DeepSeek-R1) into smaller, efficient student models.

- **Scientific Reasoning Skills**: Mimicking scientists’ problem-solving pathways, such as hypothesis generation, validation, and logical deduction.

- **Benchmarking & Applications**: Evaluated on tasks including experimental studies, chemical mechanisms, application scenarios, and industrialization challenges in MOFs research.

---

## 📊 Features

- **Multi-step reasoning** for scientific tasks (experiment design, reaction prediction, performance analysis).

- **Domain specialization** in **MOF adsorption**, catalysis, and chemical mechanism exploration.

- **High performance** compared to general-purpose LLMs (outperforming GPT-4.5, DeepSeek-R1, etc.).

- **Material recommendation ability** with accuracy comparable to Density Functional Theory (DFT).

- **Adaptability**: Easily extendable to other chemistry-related domains by incorporating domain CoT data.

---

## 📥 Model Access

- **Model weights (Hugging Face)**: [ChemReasoner-7B](https://huggingface.co/baixuefeng/ChemReasoner-7B)

- **Code repository (GitHub)**: [ChemReasoner-Code](https://github.com/MontageBai/ChemReasoner-Code)

- **Direct download (model files)**: [Download from Hugging Face](https://huggingface.co/baixuefeng/ChemReasoner-7B/resolve/main/pytorch_model.bin)

⚠️ Note: The project will soon be renamed to **MOFReasoner**, but the current release is under the name **ChemReasoner**.

---

## ⚙️ Implementation Details

### Code Organization

- **Dataset construction and cleaning** scripts are provided in the `MakeDataset/` directory.

- **Training configuration files** are provided in the `Training/` directory.

- **Evaluation scripts** are provided in the `Evaluation/` directory.

---

### Training

Model fine-tuning was performed **entirely using the official LLaMA-Factory (v5) training pipeline** with **LoRA** adaptation.  
No custom training loops were introduced beyond the standard LLaMA-Factory workflow.

---

### Inference

Inference and evaluation were carried out using **xinference (v1.4.0)** with the **vLLM backend (v0.7.2)**.

During inference, the following parameters were used:

- `temperature = 0.9`

- `max_tokens = 4096`

- `top_p = 1.0` (default value; not explicitly specified)

---

### Software Environment

The software environment was managed using a Python virtual environment.  
All dependencies are listed in `requirements.txt`.

#### Key Software Versions

- Python: 3.11.10

- PyTorch: **2.5.1**

- transformers: 4.45.2

- LLaMA-Factory: v5

- xinference: 1.4.0

- vLLM: 0.7.2

---

## 🛠️ How to Use

We recommend running MOFReasoner via **xinference**, which provides an easy deployment workflow and supports the **vLLM backend** for high-throughput inference. Direct **vLLM** usage is also supported.

### Option A. Recommended: Serve with xinference

1. Ensure the model directory contains the full Hugging Face–format files, including:
   
   - `config.json`
   
   - tokenizer files
   
   - all `model-0000x-of-0000y.safetensors` shards
   
   - `model.safetensors.index.json`

2. Start the xinference server (if not already running):

`xinference-local --host 0.0.0.0 --port 9997`

3. Launch the model using the vLLM backend:

`xinference launch \  --model-path /path/to/MOFReasoner \  --model-name mofreasoner \  --engine vllm \  --num-gpus 1`

4. Send requests through xinference (API or client). Inference parameters such as `temperature` can be specified per request.

---

### Option B. Direct vLLM (OpenAI-compatible server)

`python -m vllm.entrypoints.openai.api_server \  --model /path/to/MOFReasoner \  --tensor-parallel-size 1 \  --trust-remote-code`

---

### Notes

- Always provide the **model directory** to vLLM rather than individual shard files.

- Ensure that `model.safetensors.index.json` exists in the model directory.

---

## 📈 Performance

MOFReasoner was evaluated against leading models across four task categories:

- Experimental Studies of MOFs

- Chemical Mechanisms of adsorption

- Application Scenarios of MOF-based adsorbents

- Industrialization Challenges

Key results:

- Achieved the highest expert-evaluated score (25.5/30).

- Demonstrated reliable multi-step reasoning.

- Showed strong agreement with DFT-based validation.

---

## 📜 License

- MOFReasoner is released under the **MIT License**.

- Distilled base models retain their original licenses.

---

## 📚 Citation

`@article{bai2025mofreasoner,   title={MOFReasoner: Think Like a Scientist—A Domain-Specific Reasoning LLM via Knowledge Distillation},   author={Bai, Xuefeng and Zheng, Zhiling and Wang, Hao-Tian and Yang, Rui and Zhang, Xin and Li, Jian-Rong}, }`

---

## 📬 Contact

**Corresponding Authors**

- Prof. Jian-Rong Li, Beijing University of Technology (jrli@bjut.edu.cn)

- Prof. Xin Zhang, Beijing University of Technology (zhang.xin@bjut.edu.cn)

**Project Maintainers**

- Xuefeng Bai, Beijing University of Technology

- Zhiling Zheng, MIT
