from difflib import SequenceMatcher

def check_plagiarism(text1, text2):
    matcher = SequenceMatcher(None, text1, text2)
    similarity = matcher.ratio()
    return round(similarity * 100, 2)