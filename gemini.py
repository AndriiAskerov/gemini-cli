import os
import sys
from google import genai

def main():
    if len(sys.argv) < 2:
        print("Використання: python3 gemini.py \"Ваш запит сюди\"")
        sys.exit(1)


    prompt = " ".join(sys.argv[1:])

    # Перевірка наявності ключа у середовищі
    if not os.environ.get("GEMINI_API_KEY"):
        print("Помилка: змінна GEMINI_API_KEY не знайдена в системному середовищі.", file=sys.stderr)
        sys.exit(1)

    client = genai.Client()

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )
        print(response.text)
    except Exception as e:
        print(f"Помилка виконання запиту: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
