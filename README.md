# LLM-Lab
# Gen AI Day 1 - Ollama + Python

## Overview
A simple Generative AI project using Ollama and Llama3.2 locally.

The application sends prompts from Python to a locally running LLM and prints AI-generated responses.

## Concepts Learned
- Tokens
- Context Window
- Prompt → Response workflow
- Local LLM inference
- Python to AI model communication

## Technologies Used
- Python
- Ollama
- Llama3.2

## How It Works
Python script sends a prompt to Ollama's local server.

Flow:
Python → Ollama → Llama3.2 → Response

## Run Project

Install package:

pip install ollama

Run Ollama model:

ollama run llama3.2

Execute script:

python main.py
