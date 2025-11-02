# IRIS Homework Pipeline

## Objectives

This project sets up an IRIS homework pipeline with the following objectives:

1. **Setup GitHub Repository**:  
   - Created a GitHub repository with two branches: `dev` and `master`.

2. **Unit Tests**:  
   - Developed evaluation and data validation unit tests using `pytest`.

3. **Continuous Integration (CI)**:  
   - Configured GitHub Actions for evaluation and testing.
   - Fetched the model and data needed for evaluation from DVC (configured in previous week).

4. **Development Workflow**:  
   - Pushed pytest code changes to the `dev` branch.
   - Raised a Pull Request (PR) to merge changes into the `master` branch.

5. **Branch-Specific CI**:  
   - Ensured every branch has its own CI pipeline triggered on `push` or `PR merge`.

6. **Sanity Test with CML**:  
   - Ran a sanity test using GitHub Actions to print a report as a comment on the PR using CML.

## Getting Started

### Prerequisites
- Python 3.x
- `pytest` or `unittest`
- DVC
- GitHub Actions
- CML

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/jemma-mg/mlops-learning
   cd https://github.com/jemma-mg/mlops-learning
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure DVC to fetch the model and data:
   ```bash
   dvc pull
   ```

4. Run unit tests locally:
   ```bash
   pytest
   ```

### CI/CD Workflow
- Push changes to the `dev` branch.
- Create a Pull Request to merge into the `main` branch.
- GitHub Actions will:
  - Run unit tests.
  - Fetch model and data using DVC.
  - Execute a sanity test and post a report as a comment using CML.

### Directory Structure
```
.
├── tests/
│   ├── test_data_validation.py
│   ├── test_model_eval.py
├── .github/
│   └── workflows/
│       ├── ci.yml
├── dvc.yaml
├── requirements.txt
└── README.md
```