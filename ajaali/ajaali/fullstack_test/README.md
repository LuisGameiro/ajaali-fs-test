# AJAALI - Full Stack Developer Test

This technical test is a representation of the role you will be performing and the technologies in use. Please take your time in completing this test, there is no time limit and you can take as long as you wish. Attention to detail and good developer practices are key and your answer will be rated on the following points:
1. Project layout.
1. Code structure and formatting.
1. Use of good design patterns.
1. Attention to details on implementing the figma design.

When you've completed your answer, please share a link to the github repository.

## Brief
You have been provided a figma design by our team designer and you've been tasked with implementing this screen. The screen allows users to search for flights and sort the results.

Figma Design Link: https://www.figma.com/proto/azih5DhSF66MfnaktjyfPD/Ajaali-Flights?page-id=26%3A1920&node-id=26-1993&node-type=canvas&viewport=510%2C387%2C0.61&t=5kLALDU20n9MDud6-1&scaling=scale-down&content-scaling=fixed&show-proto-sidebar=1&starting-point-node-id=26%3A1993

> [!NOTE]
> You will need a figma account to be able to access the figma Web App.

### Stub data
Please run `flight_data_generator.py` to create the stub data.

### Technologies
#### Front End
The web app uses `htmx`, `tailwind css` and `AlpineJS`.

#### Back End
Your server needs to use `fastapi` and needs to be runnable locally.

#### Database
Your database is to be deployed on AWS Dynamo DB. You must include the CDK code to provision the dynamo db table with your response.

> [!NOTE]
> Please make sure you don't include you AWS account or API Key, but make these configurable through environment files.

## What we expect
1. A fully working python repository that can be run locally, your python project must be layed out in a way that can be shared. Using `Poetry` is preferred.
1. Your repository must include the AWS CDK stack that's used to deploy any AWS resources used.
1. The User interface must replicate the figma design provided. If a button or filter is active in the design then it should be active in your response, otherwise showing the button or filter on the design is enough.

Please provide the link to your answer once you've completed it, your profile will not be reviewed without this.

Best of luck!.
