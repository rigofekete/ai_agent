# 🐍 Python AI Code-Fixing Agent

**A small, security-conscious AI agent that analyzes Python repositories, detects bugs, and proposes or applies fixes.**

---

## 📌 Description

This project is an experimental AI-powered assistant that brings **agentic IDE-like features** into a simple Python tool.  
It uses an LLM with tool calling to:

- 🧩 Parse and summarize project context (files, errors, tests)  
- 🛠️ Generate targeted patches and refactors  
- ✅ Run tests and linting to validate changes  
- 🔁 Iterate until errors are resolved  

It’s inspired by features found in editors like Cursor, Zed, and Claude Code — but implemented from scratch for educational purposes.

---

## ✨ Features

- 🔧 **Modular tool interface** (file read/write, test runner, shell sandbox)  
- 📐 **Deterministic prompts** and configurable model/provider  
- 🛡️ **Safety rails**: scoped file access, dry-run mode, reversible changes via Git  
- 🔌 **Extensible design**: add new tools, swap LLMs, tweak prompts/strategies  

---

## 🛠️ Tech Stack

- 🐍 **Python 3.x**  
- 🤖 **LLM API** (provider-agnostic)  
- 🌲 **Git** for change tracking  
- ⚙️ Optional: integration with **pytest**, **ruff**, **black** for testing, linting, and formatting  
