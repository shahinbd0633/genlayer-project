# genlayer-project
This is my first project repository on GitHub.
# GenLayer Standalone Intelligent Contract: SimpleOracleAgreement

This repository contains a secure, reusable standalone intelligent contract built for the GenLayer network. It demonstrates real GenLayer consensus-driven web data evaluation rather than a basic hello-world or simple storage contract.

## Purpose & Use Case
The `SimpleOracleAgreement` contract allows multiple validators to securely fetch external data from a provided URL, evaluate conditions through consensus, and reach a definitive agreement state without relying on centralized oracles.

## How Consensus is Used
- **Equivalence Principle:** Validators independently execute AI-driven prompts via GenLayer's execution environment to verify external web text.
- **State Finalization:** Once the consensus threshold is met, the contract safely updates its internal state (`outcome`) and locks further modifications.

## Source Code Overview
- `contract.py`: Contains the main smart contract logic using the GenLayer Python decorator framework (`@gl.contract` and `@gl.public`).
