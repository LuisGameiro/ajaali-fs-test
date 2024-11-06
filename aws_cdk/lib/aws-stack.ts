import * as cdk from 'aws-cdk-lib';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';

export class AwsStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    const dynamoDBTable = new dynamodb.Table(this, "FlightsTable", {
      partitionKey: {
        name: "flight_id",
        type: dynamodb.AttributeType.STRING
      },
      tableName: "FlightsTable",
      billingMode: dynamodb.BillingMode.PROVISIONED,
      readCapacity: 1,
      writeCapacity: 1,
      encryption: dynamodb.TableEncryption.AWS_MANAGED,
      timeToLiveAttribute: "expiry_date",
      removalPolicy: cdk.RemovalPolicy.DESTROY,

    });
    dynamoDBTable.addGlobalSecondaryIndex({
      indexName: 'source-departure-index',
      partitionKey: { name: 'source', type: dynamodb.AttributeType.STRING },
      sortKey: { name: 'departure_dt', type: dynamodb.AttributeType.STRING },
      projectionType: dynamodb.ProjectionType.ALL,
    });
  }
}
