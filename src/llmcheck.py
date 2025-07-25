import os
import pandas as pd
from constants import DATA_PATH, SKILL_FILE_PATH
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_api_key)

def get_detailed_resume_recommendation():
    
    data_df = pd.read_excel(DATA_PATH)
    first_jd_text = data_df.loc[0, 'Text']
    jd_company = data_df.loc[0, 'Company']

    
    skill_df = pd.read_excel(SKILL_FILE_PATH)
    all_skills = []
    for col in skill_df.columns:
        all_skills += skill_df[col].dropna().tolist()
    all_skills = list(set(all_skills))  # Unique

    
    rating_df = pd.read_csv('../output/skillset.csv')
    first_row = rating_df.iloc[0]
    rating_string = ", ".join([f"{col}: {first_row[col]}" for col in rating_df.columns[1:]])

    
    prompt = f"""
You are a resume review assistant.

Below is the Job Description (JD), the candidate's skill set, and their rated skill categories.
Suggest ways to improve the candidate's resume to better align with the JD.

---

📌 Job Description (JD) from {jd_company}:
{first_jd_text}

📚 Candidate's Full Skill Set:
{', '.join(all_skills)}

📊 Skill Ratings:
{first_row['Company/Candidate Name']}: {rating_string}

---

💡 Please suggest:
1. Key missing skills from the resume
2. Certifications or courses to add
3. Action verbs or keywords to include
4. Projects to add or expand
"""

    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    recommendation = get_detailed_resume_recommendation()
    print("\n💡 Groq LLM Recommendation:\n")
    print(recommendation)
