"""Script to clean up Dependabot PR bodies.
Converts HTML to Markdown and removes "Dependabot commands and options" section.
"""

import sys
import re
import html2text

def clean_body(input_file):
    """Reads a file, removes the "Dependabot commands and options" section,
    converts the rest to Markdown, and writes it back.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    # Remove the 'Dependabot commands and options' section.
    # We assume the summary tag immediately follows the details tag.
    pattern = (
        r'<details>\s*<summary>Dependabot commands and options</summary>'
        r'[\s\S]*?</details>'
    )

    # Check if the section exists. If not, we assume it's already processed.
    if not re.search(pattern, content, flags=re.IGNORECASE):
        print("No 'Dependabot commands and options' section found. "
              "Assuming file is already cleaned.")
        return

    cleaned_content = re.sub(pattern, '', content, flags=re.IGNORECASE)

    # Initialize html2text
    h = html2text.HTML2Text()
    h.body_width = 0
    h.ignore_images = False
    h.ignore_links = False

    # Convert to Markdown
    markdown_content = h.handle(cleaned_content)

    # Write back to file
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean_dependabot_body.py <file>")
        sys.exit(1)

    clean_body(sys.argv[1])
