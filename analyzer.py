import re
from collections import Counter
import textstat

def clean_and_tokenize(text):
    words = re.findall(r'\b[a-z]+\b', text.lower())
    return words

def get_stop_words():
    return set([
        "the", "a", "an", "and", "or", "but", "in", "on", "at", "to",
        "for", "of", "with", "is", "was", "are", "were", "be", "been",
        "have", "has", "had", "do", "does", "did", "will", "would",
        "could", "should", "may", "might", "this", "that", "it", "its",
        "i", "you", "he", "she", "we", "they", "my", "your", "not", "as"
    ])

def get_word_stats(text):
    words = clean_and_tokenize(text)
    stop_words = get_stop_words()
    filtered_words = [w for w in words if w not in stop_words]
    char_len = [len(w) for w in words]

    return {
        "total_words": len(words),
        "unique_words": len(set(words)),
        "top_keywords": Counter(filtered_words).most_common(15),
        "avg_word_length": round(sum(char_len) / len(words), 2) if words else 0,
        "lexical_diversity": round(len(set(words)) / len(words), 3) if words else 0
    }

def get_sentence_stats(text):
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
    sentence_len = [len(s.split()) for s in sentences]

    return {
        "total_sentences": len(sentences),
        "avg_sentence_length": round(sum(sentence_len) / len(sentence_len), 2) if sentence_len else 0,
        "longest_sentence": max(sentence_len) if sentence_len else 0,
        "shortest_sentence": min(sentence_len) if sentence_len else 0,
    }

def get_readability(text):
    return {
        "flesch_reading_ease": textstat.flesch_reading_ease(text),
        "flesch_kincaid_grade": textstat.flesch_kincaid_grade(text),
        "reading_time_seconds": textstat.reading_time(text, ms_per_char=14.69),
    }

def get_tone_indicators(text):
    text_lower = text.lower()
    tone_keywords = {
        "Positive 😊": ["great", "excellent", "amazing", "love", "wonderful", "fantastic",
                        "good", "happy", "success", "best", "brilliant", "improve", "wow", "marvelous"],
        "Negative 😟": ["bad", "terrible", "awful", "hate", "worst", "fail", "problem",
                        "difficult", "unfortunately", "poor", "wrong", "never"],
        "Formal 🎩":   ["therefore", "furthermore", "consequently", "hereby", "whereas",
                        "shall", "pursuant", "accordingly", "notwithstanding"],
        "Urgent ⚡":   ["immediately", "urgent", "asap", "critical", "deadline", "now",
                        "must", "required", "emergency", "priority"],
    }

    scores = {}
    for tone, keywords in tone_keywords.items():
        matches = [kw for kw in keywords if kw in text_lower]
        scores[tone] = len(matches)

    dominant_tone = max(scores, key=scores.get) if any(scores.values()) else "Neutral 😐"
    return {"scores": scores, "dominant": dominant_tone}

def full_analysis(text):
    return {
        "word_statistics": get_word_stats(text),
        "sentence_statistics": get_sentence_stats(text),
        "readability": get_readability(text),
        "tone": get_tone_indicators(text),
    }