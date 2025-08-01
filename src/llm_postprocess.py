import ollama
import re

def clean_text_with_llm(raw_text: str) -> str:
    prompt = f"""
You are an assistant that extracts multiple-choice questions from raw OCR text.

The text may contain headings, dates, paper codes, group names, and other metadata.
Your job:
1. Extract only questions and their options (A, B, C, D).
2. Ignore headings, dates, marks, group names, etc.
3. Maintain proper formatting: question followed by options (each on a new line).
4. Do not invent new questions or add answers.
5. If a question is incomplete, try to reconstruct it using context, else skip it.

Here is the raw OCR text:
\"\"\"
{raw_text}
\"\"\"

Now, output only the cleaned list of questions with their options.
""".strip()

    try:
        response = ollama.chat(
            model="deepseek-r1:1.5b",
            messages=[
                {"role": "system", "content": "You are a helpful and precise text formatter."},
                {"role": "user", "content": prompt}
            ]
        )

        # ✅ Remove <think>...</think> blocks before returning
        cleaned = re.sub(r"<think>.*?</think>", "", response['message']['content'], flags=re.DOTALL)
        return cleaned.strip()

    except Exception as e:
        print(f"[ERROR] LLM processing failed: {e}")
        return ""
