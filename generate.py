from transformers import pipeline
from rake_nltk import Rake

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_key_points(content, num_points=3):
    rake = Rake()
    rake.extract_keywords_from_text(content)
    ranked_phrases = rake.get_ranked_phrases()
    return ranked_phrases[:num_points]

def generate_response(query, content, source_url):
    if not content or len(content.strip()) == 0:
        return "No content found to generate a response."
    
    # Split content into chunks of 500 tokens
    words = content.split()
    chunks = [" ".join(words[i:i + 500]) for i in range(0, len(words), 500)]
    
    summaries = []
    for chunk in chunks:
        prompt = f"Query: {query}\nEvidence: {chunk}"
        try:
            response = summarizer(prompt, max_length=100, min_length=50, do_sample=False)
            summaries.append(response[0]["summary_text"])
        except Exception as e:
            print(f"Error generating response: {e}")
    
    if summaries:
        summary = " ".join(summaries)
        return f"{summary}\n\nRead more: {source_url}"
    else:
        return "Failed to generate a response. Please try again."