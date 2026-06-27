def build_prompt(role, context, task):

    prompt = f"""
Role:
{role}

Context:
{context}

Task:
{task}
"""

    return prompt


role = "Senior QA Engineer"

context = "ISP Checkout Application"

task = "Generate Functional Test Cases"

print(build_prompt(role, context, task))
