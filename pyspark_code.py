import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

# -------------------------------------
#  Required to run the job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# -------------------------------------
#  Region filter — keep only CA, GB, US
predicate_pushdown = "region in ('ca','gb','us')"

# -------------------------------------
# Read from Glue Catalog (update if your DB/table names differ)
datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database = "de-on-youtube-raw",
    table_name = "raw_statistics",
    transformation_ctx="datasource0",
    push_down_predicate=predicate_pushdown
)

# -------------------------------------
# Apply schema mapping
applymapping1 = ApplyMapping.apply(
    frame=datasource0,
    mappings=[
        ("video_id", "string", "video_id", "string"),
        ("trending_date", "string", "trending_date", "string"),
        ("title", "string", "title", "string"),
        ("channel_title", "string", "channel_title", "string"),
        ("category_id", "long", "category_id", "long"),
        ("publish_time", "string", "publish_time", "string"),
        ("tags", "string", "tags", "string"),
        ("views", "long", "views", "long"),
        ("likes", "long", "likes", "long"),
        ("dislikes", "long", "dislikes", "long"),
        ("comment_count", "long", "comment_count", "long"),
        ("thumbnail_link", "string", "thumbnail_link", "string"),
        ("comments_disabled", "boolean", "comments_disabled", "boolean"),
        ("ratings_disabled", "boolean", "ratings_disabled", "boolean"),
        ("video_error_or_removed", "boolean", "video_error_or_removed", "boolean"),
        ("description", "string", "description", "string"),
        ("region", "string", "region", "string")
    ],
    transformation_ctx="applymapping1"
)

# -------------------------------------
# Resolve mixed types / structs
resolvechoice2 = ResolveChoice.apply(
    frame=applymapping1,
    choice="make_struct",
    transformation_ctx="resolvechoice2"
)

# Drop null fields
dropnullfields3 = DropNullFields.apply(
    frame=resolvechoice2,
    transformation_ctx="dropnullfields3"
)

# -------------------------------------
# Coalesce to 1 file per partition (optional, good for small test data)
datasink1 = dropnullfields3.toDF().coalesce(1)
df_final_output = DynamicFrame.fromDF(datasink1, glueContext, "df_final_output")

# -------------------------------------
# Write to cleansed bucket in Parquet format
datasink4 = glueContext.write_dynamic_frame.from_options(
    frame=df_final_output,
    connection_type="s3",
    connection_options={
        "path": "s3://de-on-youtube-cleansed-useast1-dev-g3/youtube/raw_statistics/",  
        "partitionKeys": ["region"]
    },
    format="parquet",
    transformation_ctx="datasink4"
)


job.commit()
