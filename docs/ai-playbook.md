# AI Usage Playbook

## When I Reach for AI First
* Generating repetitive test boilerplate and test case scaffolding.
* Formatting Markdown tables, documentation files, and technical logs.
* Explaining dense stack traces or framework deprecation warnings.

## When I Do Not Reach for AI First
* Designing initial core system architecture and database schema relationships.
* Writing security, authentication, and authorization logic.
* Debugging complex state management issues across container boundaries.

## My Non-Negotiables
* All AI-generated code must be manually reviewed and tested locally via `pytest`.
* Secrets, API keys, and private credentials must never be passed to AI prompts.
* No code suggested by an AI gets merged if it violates core project architecture.

## My Review Rules
* Check for hallucinated dependencies or unnecessary external libraries.
* Verify that suggested edits stay strictly within the targeted scope.
* Run unit tests immediately after applying any AI-assisted refactor.

## What I Am Still Figuring Out
* Constructing optimal prompt constraints for Docker multi-stage build optimization.
* Integrating pre-commit hooks to automatically check AI code against project styling rules.

## Decision Card
* **Use AI?** YES — If the task involves boilerplate generation, documentation formatting, or syntax queries.
* **Use AI?** NO — If the task alters core domain logic, security boundary rules, or database models.