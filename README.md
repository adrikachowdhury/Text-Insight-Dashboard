# 🔍 Text Insight Dashboard

A web app that performs deep linguistic analysis on any text -
built with pure Python (no ML libraries), deployed with Streamlit.

🔗 **Live Demo:** [Text Insight Dashboard](https://text-insight-dash.streamlit.app)

<img width="500" height="711" alt="1" src="https://github.com/user-attachments/assets/9914ee8d-b6c2-4185-af01-d22bde931a4c" /><img width="500" height="530" alt="2" src="https://github.com/user-attachments/assets/c481d2d7-176a-4a0e-92e5-263ffcb17eb2" /><img width="500" height="543" alt="3" src="https://github.com/user-attachments/assets/9e2989fb-f223-4836-ad20-a5c96ef231ec" /><img width="500" height="690" alt="4" src="https://github.com/user-attachments/assets/d723aaf3-d163-4d7e-a8d2-77b8b8dcf991" />

## 💡 How This Project Started

This project was build with the intention to deeply understand text processing at a fundamental level, before jumping into ML libraries and pre-built models.

## 🧩 The Problem

Most people write without really knowing how their writing comes across. 

- Is this email sounding too formal or too negative?
- Will my target audience actually understand this article?
- Am I repeating the same words too often?

Professional tools like Grammarly exist, but they're black boxes - they 
give us a score without explaining *why*. And for a student, a 
content writer, a researcher, or someone learning English, we deserve 
to understand what's actually happening inside the given text.

This project was built to solve exactly that. It gives you a transparent, 
explainable breakdown of the writing - no subscriptions, no black boxes, 
no ML magic. Just an honest analysis anyone can actually learn from.

---

## ✨ What It Does

Paste any huge text - be it an article, an essay, an email, a speech, or a dissertation 
chapter - and instantly get:

### 📊 Summary Statistics
- Total word count and unique word count
- Total number of sentences
- Average word length and average sentence length
- **Lexical Diversity Score** - measures how varied the vocabulary is.
  A score closer to 1.0 means we're using a wide range of words. 
  A low score means a lot of repetition is happening.
- Estimated reading time

### 📖 Readability Analysis
- **Flesch Reading Ease Score** (0–100): Higher = easier to read.
  Developed in 1948 and still used by governments, publishers, and 
  insurance companies to ensure documents are understandable.
- **Flesch-Kincaid Grade Level**: Maps a text's difficulty to a 
  US school grade level. Grade 8 means an average 8th grader can 
  understand it. Grade 16 means university level.
- An interactive gauge chart that visualises difficulty at a glance

### 🎭 Tone Detection
- Rule-based tone detection across four categories:
  **Positive**, **Negative**, **Formal**, and **Urgent**
- Detects which tone dominates the text based on keyword matching
- No ML - fully transparent and explainable

### 🔑 Keyword Frequency
- Extracts the most meaningful words after removing stop words
  (common words like "the", "is", "a" that don't have any meaning)
- Horizontal bar chart with colour-coded frequency

### 📝 Sentence Complexity
- Bar chart showing the word count of each individual sentence
- Spikes in the chart reveal where your text becomes complex or heavy

### 📥 Downloadable Report
- Export a clean `.txt` summary of all your results with one click

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Streamlit | Web app framework - turns Python into a browser UI |
| Plotly | Interactive charts (gauge, bar charts) |
| Textstat | Readability scoring (Flesch formulas, reading time) |
| Regex (`re`) | Text tokenization and sentence splitting |
| Collections (`Counter`) | Word frequency counting |

**No machine learning libraries were used.** Everything here is 
built on rule-based logic and statistical formulas. This is intentional - 
the goal was to deeply understand what happens to text *before* handing 
it to a model.

---

## 🚀 Run It Locally

**Step 1 - Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/Text-Insight-Dashboard.git
cd text-insight-dashboard
```

**Step 2 - Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 3 - Launch the app**
```bash
streamlit run app.py
```

**Step 4 (Optional) - Run the Notebook**

If you want to test this out on a notebook like the Google Colab, then try with `analyzer_colab.ipynb`.

---

## 📁 Project Structure
```
text-insight-dashboard/
│
├── app.py                     # Streamlit UI - all layout and visual logic
├── analyzer.py                # Analysis engine - all text processing functions
├── analyzer_colab.ipynb       # Whole implementation in notebook
├── requirements.txt           # Dependencies
└── README.md                  # You are here
```

The project is deliberately split into two files. `analyzer.py` is 
pure Python with no UI code - it just takes text and returns results. This file basically contains all the functions required to process a text before analyzing it.
`app.py` is pure UI code - it just takes results and displays them. 
This separation of concerns is a real software design principle, and 
keeping it this way makes both files easy to read, test, and extend.

---

## 🧠 What I Learned Building This

This was my first proper project-based learning with this end-to-end Python project, which integrates a deployed web UI, and it taught me more than I expected:

- How **regex patterns** work for extracting words and splitting sentences
- What **lexical diversity** actually means mathematically
- How readability formulas like **Flesch-Kincaid** are calculated 
  (syllables, word length, sentence length - all combined into a formula)
- How **stop word removal** changes frequency analysis completely
- How **textstat** works amazingly in calculating every possible statistic of a text
- How **Plotly** builds interactive charts vs static ones
- How to **separate logic from UI** in a real project

---

## 🙏 Acknowledgements

The project idea and learning roadmap were suggested by 
**Claude (Anthropic's AI assistant)**, which I'm currently using as an AI mentor 
to dig deeper into NLP from scratch. This js not just for explanations, but for building **theoretical understanding**, exploring **structured project ideas**, and **working through code step by step** with **careful analysis** and **documentation**.

This project was part of my project-based learning path- building something real and deployable using only foundational 
Python knowledge - before touching any ML frameworks, and understand each crucial segment of it.

What I came away with isn't just a deployed app. It's a genuine 
understanding of regex, readability formulas, Plotly charts, Streamlit 
architecture, and how to separate logic from UI in a real project.

To those interested in digging into AI/NLP and looking for a structured path, 
I'd genuinely recommend using an AI assistant as a mentor alongside 
traditional resources. I believe, the ability to ask "why does this work?" 
after every single line of code is something textbooks can't match.

---

## 💫 Credits
Feel free to explore the documentation, and please give **credit to the owner** when using content from this repo! 
Many thanks!🙌

---

## 📬 Connect

If you found this useful or you're on a similar learning journey or for any collaboration for project-based learning, feel free to connect:

- GitHub: [@adrikachowdhury](https://github.com/adrikachowdhury)
- LinkedIn: [Adrika Chowdhury](https://linkedin.com/in/adrika-chowdhury-a582712b1/)

---
*Built while learning. Shared for anyone else who's learning too.*
