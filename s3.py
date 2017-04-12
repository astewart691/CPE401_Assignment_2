import boto3


def main():
    access_key = 'AKIAJFBFVOYWJ24UIHIA'

    secret_key = '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'

    s3 = boto3.resource('s3')

    # s3.create_bucket(Bucket = 'cpe401', CreateBucketConfiguration = {'LocationConstraint': 'us-west-1'})

    for bucket in s3.buckets.all():

        print(bucket.name)

    data = open('README.txt', 'rb')

    s3.Bucket('cpe401').put_object(Key = 'README.txt', Body = data)


main()
