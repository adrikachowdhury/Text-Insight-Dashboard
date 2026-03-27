# replaces your dashboard(), visuals(), and display() functions

import re
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from analyzer import full_analysis  # importing analysis.py functions into this Streamlit app

# STREAMLIT CONCEPT 1: st.set_page_config()
# This MUST be the very first Streamlit command in the file.
# It sets the browser tab title, icon, and layout width.
# layout="wide" uses full screen width instead of a narrow centered column.

st.set_page_config(
    page_title="Text Insight Dashboard",
    page_icon="🔍",
    layout="wide"
)

# STREAMLIT CONCEPT 2: st.title() and st.markdown()
# st.title()    → big H1 heading
# st.markdown() → renders markdown text (bold, italic, links, etc.)
# st.divider()  → draws a horizontal line to separate sections

st.title("🔍 Text Insight Dashboard")
st.markdown("Paste any text below - an article, essay, email, or speech - and get instant deep analysis.")
st.divider()

# STREAMLIT CONCEPT 3: st.text_area()
# replaces `input()` call for multi-line text input in the browser.

# Parameters:
#  label       → the text shown above the box
#  value       → default text pre-filled in the box
#  height      → pixel height of the text box
#  placeholder → hint text shown when the box is empty

# Whatever the user types is stored in `text_input`.
# Every time the user changes the text, Streamlit reruns the entire script from top to bottom automatically.

# sample_text = """Artificial Intelligence is transforming industries at an unprecedented Pace.
# Companies that fail to adapt will unfortunately fall behind. The opportunities
# are tremendous for those who embrace change. However, the challenges are equally
# significant. Building great AI systems requires not just technical expertise,
# but also a deep understanding of human needs and ethical considerations. Now,
# What Should Be Done? Therefore, leaders must act immediately to implement these
# critical changes across their organizations."""

text_input = st.text_area(
    "📋 Paste your text here:",
    height=200,
    placeholder="Type or paste any text..."
)

# STREAMLIT CONCEPT 4: st.button()- Creates a clickable button.
# type="primary" makes it blue/prominent.
# use_container_width=True stretches it full width.

# Returns True only in the moment the user clicks it.
# On the next rerun (when user hasn't clicked), it returns False.
# That's why we wrap everything inside `if analyze_btn:`-
# so the analysis only runs after the button is clicked.

analyze_btn = st.button("✨ Analyze Text", type="primary", use_container_width=True)

# Everything inside this `if` block only runs when
# the button has been clicked AND text is not empty.

if analyze_btn and text_input.strip():

    # Run all the analysis functions
    results = full_analysis(text_input)
    ws   = results["word_statistics"]
    ss   = results["sentence_statistics"]
    rd   = results["readability"]
    tone = results["tone"]

    st.divider()

    # STREAMLIT CONCEPT 5: st.columns()
    # Splits the page into side-by-side columns.
    # st.columns(5) creates 5 equal-width columns.
    # You assign each column to a variable (col1, col2, ...)
    # Then use col1.metric(...) to put content in that column.

    # This replaces your print() calls for the summary stats.

    st.subheader("📊 At a Glance")
    col1, col2, col3, col4, col5 = st.columns(5)

    # STREAMLIT CONCEPT 6: st.metric() / col.metric()
    # Displays a big number with a label above it.

    # label  → text shown above the number
    # value  → the number shown in large text
    # help   → tooltip shown when user hovers over (?) icon

    col1.metric("Total Words",     ws["total_words"])
    col2.metric("Unique Words",    ws["unique_words"])
    col3.metric("Sentences",       ss["total_sentences"])
    col4.metric("Lexical Diversity", ws["lexical_diversity"],
                help="How varied vocabulary is. 1.0 = every word unique.")

    reading_secs = rd["reading_time_seconds"]
    mins = int(reading_secs // 60)
    secs = int(reading_secs % 60)
    col5.metric("Reading Time", f"{mins}m {secs}s")

    st.divider()

    # STREAMLIT CONCEPT 7: Two-column layout for charts
    # st.columns(2) creates two equal halves.
    # We use `with col_left:` context manager to say
    # "put everything indented under this into the left column".

    col_left, col_right = st.columns(2)

    # LEFT COLUMN: Readability
    with col_left:
        # st.subheader() → medium heading (H3 level)
        # st.markdown()  → supports color text using :color[text] syntax
        # e.g.: green[Easy ✅] renders in green

        st.subheader("📖 Readability")

        ease  = rd["flesch_reading_ease"]
        grade = rd["flesch_kincaid_grade"]

        if ease >= 90:
            ease_label, ease_color = "Very Easy to Read ✅", "green"
        elif ease >= 80:
            ease_label, ease_color = "Easy to Read ✅", "green"
        elif ease >= 70:
            ease_label, ease_color = "Fairly Easy 🟡", "orange"
        elif ease >= 60:
            ease_label, ease_color = "Standard 🟡", "orange"
        elif ease >= 50:
            ease_label, ease_color = "Fairly Difficult 🔴", "red"
        elif ease >= 30:
            ease_label, ease_color = "Difficult 🔴", "red"
        else:
            ease_label, ease_color = "Very Confusing 🔴", "red"

        # st.markdown() with f-strings lets us put live variables
        # inside formatted text. The :{ease_color}[...] syntax
        # renders text in that color (Streamlit feature).

        st.markdown(f"**Reading Ease:** `{ease:.2f}` — :{ease_color}[{ease_label}]")
        st.markdown(f"**Grade Level:** US Grade `{grade:.2f}`")
        st.markdown(f"**Avg Sentence Length:** `{ss['avg_sentence_length']}` words")
        st.markdown(f"**Avg Word Length:** `{ws['avg_word_length']}` characters")

        # STREAMLIT CONCEPT 8: st.plotly_chart()
        # This is the ONLY change needed to display Plotly charts.
        # fig1.show() -> st.plotly_chart(fig1)

        # use_container_width=True makes the chart fill the column.
        # Without it, the chart uses its own fixed pixel width.

        fig1 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=ease,
            title={"text": "Reading Ease (0=Hard, 100=Easy)"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar":  {"color": "royalblue"},
                "steps": [
                    {"range": [0, 30],   "color": "#ff4b4b"},
                    {"range": [30, 60],  "color": "#ffa500"},
                    {"range": [60, 100], "color": "#21c354"},
                ],
            }
        ))
        fig1.update_layout(height=280, margin=dict(t=40, b=10))
        st.plotly_chart(fig1, use_container_width=True)  # ← replaces fig1.show()

    # RIGHT COLUMN: Tone
    with col_right:
        st.subheader("🎭 Tone Analysis")
        st.markdown(f"**Dominant Tone Detected:** `{tone['dominant']}`")

        tone_names  = list(tone["scores"].keys())
        tone_values = list(tone["scores"].values())

        fig3 = px.bar(
            x=tone_names,
            y=tone_values,
            color=tone_names,
            title="Tone Indicator Strengths",
            labels={"x": "Tone", "y": "Keyword Matches"},
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig3.update_layout(showlegend=False, height=350)
        st.plotly_chart(fig3, use_container_width=True)  # ← replaces fig3.show()

    st.divider()

    # KEYWORD FREQUENCY
    st.subheader("🔑 Top Keywords (stop words removed)")

    if ws["top_keywords"]:
        keywords, counts = zip(*ws["top_keywords"])
        fig2 = px.bar(
            x=list(counts),
            y=list(keywords),
            orientation="h",
            color=list(counts),
            color_continuous_scale="Blues",
            title="Most Frequent Meaningful Words",
            labels={"x": "Frequency", "y": "Keyword"}
        )
        fig2.update_layout(yaxis={"categoryorder": "total ascending"}, height=420)
        st.plotly_chart(fig2, use_container_width=True)  # ← replaces fig2.show()

    st.divider()

    # SENTENCE COMPLEXITY
    st.subheader("📝 Sentence Complexity Breakdown")

    sentences    = [s.strip() for s in re.split(r'[.!?]+', text_input) if s.strip()]
    sent_lengths = [len(s.split()) for s in sentences]
    sent_labels  = [f"S{i+1}" for i in range(len(sentences))]

    fig4 = px.bar(
        x=sent_labels,
        y=sent_lengths,
        color=sent_lengths,
        color_continuous_scale="Teal",
        title="Word Count per Sentence",
        labels={"x": "Sentence", "y": "Word Count"}
    )
    st.plotly_chart(fig4, use_container_width=True)  # ← replaces fig4.show()

    # STREAMLIT CONCEPT 9: st.download_button()
    # Creates a button that lets the user download a file.
    # label       → button text
    # data        → the content of the file (as a string here)
    # file_name   → what the downloaded file will be called
    #
    # No equivalent in Colab — this is a pure Streamlit feature.

    st.divider()
    report = f"""TEXT INSIGHT REPORT
====================
Total Words        : {ws['total_words']}
Unique Words       : {ws['unique_words']}
Lexical Diversity  : {ws['lexical_diversity']}
Sentences          : {ss['total_sentences']}
Avg Sentence Len   : {ss['avg_sentence_length']} words
Reading Ease Score : {rd['flesch_reading_ease']:.2f}
Grade Level        : {rd['flesch_kincaid_grade']:.2f}
Dominant Tone      : {tone['dominant']}
Top Keywords       : {', '.join([kw for kw, _ in ws['top_keywords'][:5]])}
"""
    st.download_button(
        "📥 Download Report as .txt",
        data=report,
        file_name="text_insight_report.txt"
    )

# STREAMLIT CONCEPT 10: st.warning()
# Shows a yellow warning box.
# Only shown if button was clicked but text box was empty.
# Other alert types: st.error() (red), st.success() (green), st.info() (blue)

elif analyze_btn:
    st.warning("Please paste some text first!")
