# Introduction to Natural Language Processing (NLP)
## 📖 Course Overview
This course provides a comprehensive introduction to the field of Natural Language Processing, exploring how artificial intelligence can understand, interpret, and generate human language. The curriculum covers foundational concepts from traditional text processing to modern deep learning architectures, focusing on the bridge between linguistic theory and practical AI applications.

**One-line Summary:** An introductory course on NLP fundamentals and sequence modeling, culminating in a specialized project on fine-tuning PP-OCRv5-det for historical Vietnamese script detection using the NomNaOCR dataset.

## 🔬 Final Lab Project: Vietnamese Nom Script Detection
The highlight of the course is a hands-on final project focused on Optical Character Recognition (OCR) for low-resource and historical scripts, specifically Hán-Nôm (Ancient Vietnamese characters).

**Project Scope:**
Instead of building a system from scratch, this project emphasizes Transfer Learning and Model Optimization for specialized datasets.

**Key Technical Implementation:**
Base Model: Utilizing PP-OCRv5-det, the state-of-the-art text detection model from the PaddleOCR ecosystem, known for its balance between efficiency and accuracy.

**Task:** Fine-tuning the detection module to adapt to the unique spatial characteristics and stroke complexities of Hán-Nôm characters.

**Dataset:** Leveraging NomNaOCR, a specialized dataset for Vietnamese Nom script, to improve the model's ability to localize text in historical documents.

**Objective:** To achieve high-precision text region localization, providing a robust foundation for subsequent character recognition stages in the preservation of Vietnamese cultural heritage.

## 🛠 Tech Stack & Tools
Deep Learning Framework: PaddlePaddle / PyTorch.

Core Library: PaddleOCR (PP-OCRv5).

Techniques: Fine-tuning, Data Augmentation, Model Evaluation (Precision, Recall, Hmean).

Dataset: NomNaOCR.
