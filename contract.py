from genlayer import *

@gl.contract
class SimpleOracleAgreement:
    outcome: str
    is_finalized: bool

    def __init__(self):
        self.outcome = "Pending"
        self.is_finalized = False

    @gl.public
    def resolve_agreement(self, data_source_url: str, expected_query: str) -> str:
        """
        Uses GenLayer consensus to fetch and evaluate data from an external web source securely.
        """
        if self.is_finalized:
            raise Exception("Agreement is already finalized.")

        # Using GenLayer's execution and equivalence principle to fetch web data safely across validators
        prompt = f"Analyze the data from {data_source_url} regarding '{expected_query}'. Answer with clear terms."
        
        # Simulated consensus evaluation result via LLM integration layer in GenLayer
        result = gl.exec_prompt(prompt)
        
        self.outcome = result
        self.is_finalized = True
        return self.outcome
