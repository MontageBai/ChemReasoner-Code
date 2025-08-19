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

## ⚙️ How to Use

You can run the model directly from Hugging Face using [vLLM](https://github.com/vllm-project/vllm) or [SGLang](https://github.com/sgl-project/sglang).  

### Example with vLLM

```bash
vllm serve baixuefeng/ChemReasoner-7B --tensor-parallel-size 2 --max-model-len 32768 --enforce-eager
```

### Example with SGLang

```bash
python3 -m sglang.launch_server --model baixuefeng/ChemReasoner-7B --trust-remote-code --tp 2
```

---

## 📈 Performance

MOFReasoner was evaluated against leading models (DeepSeek, Qwen, GPT series, etc.) across **four major task categories**:

- **Experimental Studies** of MOFs  
- **Chemical Mechanisms** of adsorption  
- **Application Scenarios** of MOF-based adsorbents  
- **Industrialization Challenges**

Highlights:

- Achieved the **highest expert-evaluated score (25.5/30)**, outperforming GPT-4.5, o1-preview, and DeepSeek-R1.  
- Provided **more accurate and reliable reasoning chains**, avoiding serious errors common in general-purpose models.  
- Demonstrated **robust material recommendation**, consistent with DFT validation.  

---

## 📜 License

- MOFReasoner is released under the **MIT License**.  
- Distilled base models (Qwen, LLaMA) retain their original licenses (Apache 2.0 / LLaMA license).

---

## 📚 Citation

If you use MOFReasoner in your research, please cite:

```bibtex
@article{bai2025mofreasoner,
  title={MOFReasoner: Think Like a Scientist—A Domain-Specific Reasoning LLM via Knowledge Distillation},
  author={Bai, Xuefeng and Zheng, Zhiling and Wang, Hao-Tian and Yang, Rui and Zhang, Xin and Li, Jian-Rong},
}
```

---

## 📬 Contact

- **Corresponding Authors**:  
  
  - Prof. Jian-Rong Li, Beijing University of Technology (jrli@bjut.edu.cn)  
  - Prof. Xin Zhang, Beijing University of Technology (zhang.xin@bjut.edu.cn)  

- **Project Maintainers**:  
  
  - Xuefeng Bai (Beijing University of Technology)  
  - Zhiling Zheng (MIT)  
