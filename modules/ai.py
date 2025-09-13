from openai import OpenAI
from modules.config.configuration import config


class OpenRouter:
    def __init__(self) -> None:
        self.model = "mistralai/mistral-small-3.2-24b-instruct:free"
        self.auth: str | None = config.openrouter_api_key

    def llm(self, author_has_llm_query, author_wants_llm_query, title) -> str | None:
        prompt = (
            f"Does this search query \"Seller has {author_has_llm_query}, seller wants {author_wants_llm_query}\" match this listing title \"{title}\"? "  # noqa: E501
            f"Carefully analyze the listing title and the search query. Use semantic and not literal reasoning. "
            f"For example, \"fast CPU\" is likely looking for listings that have a fast CPU for sale, not listings with the exact words \"fast CPU\" in the title. "  # noqa: E501
            f"Reply ONLY with \"TRUE\" if it matches or \"FALSE\" if not. No explanations or reasoning."
        )

        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=self.auth,
        )

        completion = client.chat.completions.create(
            extra_headers={},
            extra_body={},
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ],
        )

        return completion.choices[0].message.content

    def is_match(self, llm_response: str | None) -> bool:
        if llm_response is None:
            return False
        else:
            if "true" in llm_response.strip().lower():
                return True
            else:
                return False
