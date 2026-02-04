# Deep Learning for Natural Language Processing (NLP)

This repository covers the evolution of NLP, from classic sequence models to the latest advancements in Large Language Models (LLMs), Transformers, and Knowledge Transfer.

## Deliverable Practices

### 1. Sequence-to-Sequence & Attention Mechanisms
Implementation of deep learning architectures for complex linguistic tasks:
* **Neural Machine Translation:** Building encoder-decoder models to translate text between languages.
* **Text Summarization:** Using encoder-decoder models to generate concise summaries.
* **Architecture Study:** Visualization of attention mechanisms.


### 2. Reddit Intelligence: End-to-End NLP Pipeline
A project focused on extracting and analyzing social media data using NLP techniques.

#### Project Stages:
1. **Corpus Compilation:** Automated compilation of threads and comments across diverse subreddits using the Reddit API to build a custom text dataset.
2. **Topic Classification:** Categorizing threads into specific subreddits or themes.
3. **Subjectivity Analysis:** Detecting sentiment and opinion levels in user comments.
4. **Abstractive Summarization:** Generating concise summaries of long discussion threads using Transformer-based models.
5. **Advanced Moderation:** Implementing Zero-Shot (ZSL), Few-Shot Learning (FSL), and Chain-of-Thought (CoT) prompting for detecting inappropriate content.
6. **QA & Fine-Tuning:** Developing a Question Answering system using Instructed Fine-Tuning to interact with the compiled data.



## Tech Stack
* **Language:** Python.
* **Format:** Jupyter Notebooks (.ipynb).
* **Deep Learning:** `PyTorch`.
* **NLP Power Tools:** `Hugging Face (Transformers)`.
* **APIs:** Reddit API (PRAW).

## Repository Contents
* `Class-Exercises/`: Focused notebooks on theoretical foundations.
* `Practices/`: The core projects involving complex architectures and the Reddit case study.

## AI Relevance
* **Generative AI:** Knowledge of how modern LLMs are optimized and prompted for specific tasks.
* **Efficiency:** Mastering Transfer Learning to adapt massive models to niche domains (like specific Reddit communities).
* **Real-world Data:** Handling Reddit content proves the ability to deal with slang, sarcasm, and unstructured data.
