# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Convert and streamline description bodies of Dependabot PRs."""

import os
import re
import sys

import html2text


def process_text(content):
    """Take PR description body and clean it.

    Cleaning steps applied:
    * Remove the section "Commits"
    * Convert HTML to Markdown
    * Remove the section "Dependabot commands and options"
    """

    # Remove Commits & Changelog 1st because they're easier to find in HTML.
    content = re.sub(
        r"<details>\s*<summary>Commits</summary>.*?</details>\s*(<br\s*/?>)?",
        "",
        content,
        flags=re.DOTALL | re.IGNORECASE,
    )
    content = re.sub(
        r"<details>\s*<summary>Changelog</summary>.*?</details>\s*(<br\s*/?>)?",
        "",
        content,
        flags=re.DOTALL | re.IGNORECASE,
    )

    html_converter = html2text.HTML2Text()
    html_converter.body_width = 0
    markdown_content = html_converter.handle(content)

    # Remove the compatibility score and everything below it. If it's present,
    # this will remove everything we don't care about, and we'll be done.
    markdown_content = re.sub(
        r"[![Dependabot compatibility score].*",
        "",
        markdown_content,
        flags=re.DOTALL | re.IGNORECASE,
    )

    # Not all Dependabot PRs have a score badge. As a backup, look for the
    # paragraph after the badge, and remove that and everything below it.

    target_phrase = "Dependabot will resolve any conflicts with this PR"
    parts = markdown_content.rsplit(target_phrase, 1)
    markdown_content = parts[0].strip()

    return markdown_content


def clean_body(file_path):
    """Reads the file, cleans the text, and writes it back to the same file."""
    with open(file_path, "r") as f:
        content = f.read()

    markdown_content = process_text(content)

    # Write back to file.
    with open(file_path, "w") as f:
        f.write(markdown_content)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        script_name = os.path.basename(sys.argv[0])
        print(f"Usage: python3 {script_name} FILE")
        sys.exit(1)
    clean_body(sys.argv[1])
