from pathlib import Path

def load_prompt(prompt_name):
    """
    Load a prompt template from the Prompts/prompts folder.
    """
    # Go up one level from the python/ folder to the root, then into Prompts/prompts/
    prompt_path = Path(__file__).parent.parent / "Prompts" / "prompts" / prompt_name

    with open(prompt_path, "r") as file:
        return file.read()


prompt = load_prompt("qa_engineer.md")

print(prompt)
