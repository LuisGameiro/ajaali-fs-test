# Project Title

Brief description of what your project does and its purpose.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- Poetry (`pip install poetry`)
- AWS CLI configured
- AWS CDK installed (`npm install -g aws-cdk`)

## Setup
 
1. Create the .env your environment variables.


## Deploying with AWS CDK

1. Synthesize the CloudFormation template:
    ```bash
    cdk synth
    ```

2. Deploy the stack:
    ```bash
    cdk deploy
    ```

## Setting Up the Environment

1. Create and activate a virtual environment:
    ```bash
    poetry shell
    ```

2. Install dependencies:
    ```bash
    poetry install
    ```

3. Start the FastAPI server:
    ```bash
    poetry run start
    ```
