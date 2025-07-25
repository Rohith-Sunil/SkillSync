
# SkillSync AI

SkillSync AI is an intelligent Job Description (JD) parser and Resume analyzer built using spaCy and Groq's large language models. It extracts key skills from resumes and job descriptions, compares them, and uses LLMs to recommend personalized resume improvements.

## 🔍 Features

- Extract skills and sub-skills from resumes and JDs using spaCy PhraseMatcher
- Organize and visualize skill coverage across domains
- Match resumes against JDs and detect missing skills
- Use Groq LLMs to recommend:
  - Missing skills
  - Certifications or tools to learn
  - Action verbs and phrasing
  - Project ideas to improve resumes

## 📂 Folder Structure

```
Resume_JD_Parser/
├── input/                  # Contains Data.xlsx and Skillset.xlsx
├── output/                 # Generated CSVs and charts
├── src/
│   ├── func.py             # Skill extraction and plotting functions
│   ├── init_parser.py      # PhraseMatcher setup
│   ├── spaCy_parser.py     # Main extraction pipeline
│   ├── llmcheck.py         # Groq LLM-based recommendations
│   ├── constants.py        # File paths
│   └── .env                # Contains GROQ_API_KEY
```

## 🛠️ Requirements

- Python 3.7+
- See `requirements.txt` for dependencies

Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Run the Project

1. Place your job descriptions and resumes in `input/Data.xlsx`
2. List your categorized skills in `input/Skillset.xlsx`
3. Run the main pipeline:

```bash
python src/spaCy_parser.py
```

4. (Optional) Run LLM-based feedback:

```bash
python src/llmcheck.py
```

## 🔐 Environment Variables

Create a `.env` file in `src/` with:

```
GROQ_API_KEY=your-api-key-here
```

## 📊 Outputs

- `output/Data.csv` – Matched skill data
- `output/skillset.csv` – Pivoted skill matrix
- `output/graph.png` – Visual skill comparison
- `output/recommendation_*.txt` – LLM suggestions

## 🧠 Powered by

- spaCy for NLP & matching
- Groq (Mixtral/LLaMA3) for resume optimization suggestions

## 📄 License

MIT License
