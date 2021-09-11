from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = 'static'
    defaul_acl = 'private'

class PublicMediaStorage(S3Boto3Storage):
    location = 'media'
    defaul_acl = 'private'
    file_overwrite = False