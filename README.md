# UserFinder 🔍

A lightweight, ethical OSINT tool to check if a username exists across public platforms.

> ⚠️ **For educational and authorized reconnaissance only. Do not use for harassment or unauthorized investigations.**

[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## ✨ Features
- Check 10+ platforms instantly
- Clean CLI output with [Rich](https://github.com/Textualize/rich)
- Easy to add new sites (just edit `sites.json`!)
- Respects servers (adds delays, uses polite User-Agent)

## 🚀 Install & Run
```bash
git clone https://github.com/yourname/userfinder.git
cd userfinder
pip install requests rich

python main.py username#
