import ollama

def generate_slide_content(text, question):

    prompt = f"""
You are an expert presentation designer.

Create a 5 slide presentation using SHORT bullet points.

Rules:
- Each bullet must be maximum 10 words
- Maximum 4 bullets per slide
- No paragraphs
- Clear presentation style

Format exactly like this:

**Slide 1: Title**
- bullet
- bullet
- bullet

**Slide 2: Title**
- bullet
- bullet
- bullet

**Slide 3: Title**
- bullet
- bullet
- bullet

**Slide 4: Title**
- bullet
- bullet
- bullet

**Slide 5: Summary**
- bullet
- bullet
- bullet

Document Content:
{text}

User Question:
{question}
"""

    response = ollama.chat(
        # model="llama3",
        model="phi3",
        # model="llama3:8b",
        # model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]