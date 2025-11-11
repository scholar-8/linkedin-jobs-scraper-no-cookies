thondef clean_text(text):
"""Cleans the extracted text."""
return text.strip().replace("\n", " ").replace("\r", "")