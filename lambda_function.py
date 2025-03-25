import awswrangler as wr
import pandas as pd
import urllib.parse
import os

# Environment variables
os_input_s3_cleansed_layer = os.environ['s3_cleansed_layer']
os_input_glue_catalog_db_name = os.environ['glue_catalog_db_name']
os_input_glue_catalog_table_name = os.environ['glue_catalog_table_name']
os_input_write_data_operation = os.environ['write_data_operation']


def lambda_handler(event, context):
    # Extract bucket and key from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    try:
        # Read JSON from S3
        df_raw = wr.s3.read_json(f's3://{bucket}/{key}')

        # Normalize nested 'items' field into flat table
        if 'items' in df_raw:
            df_step_1 = pd.json_normalize(df_raw['items'])
        else:
            print("No 'items' field found in the JSON")
            return {"status": "failed", "reason": "Missing 'items' key in JSON"}
        
       
        

        # Write DataFrame to S3 as Parquet and catalog it in AWS Glue
        wr_response = wr.s3.to_parquet(
            df=df_step_1,
            path=os_input_s3_cleansed_layer,
            dataset=True,
            mode=os_input_write_data_operation,
            database=os_input_glue_catalog_db_name,
            table=os_input_glue_catalog_table_name
        )

        print("Write successful:", wr_response)
        return wr_response

    except Exception as e:
        print(f"Exception occurred: {e}")
        print(f"Error processing object {key} from bucket {bucket}")
        raise e
