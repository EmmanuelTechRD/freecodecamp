# freeCodeCamp challenge: Database Migration
# Given two database objects, return the second object with any missing properties from the first filled in.
# Fields that already exist in the record should not be overwritten.
def migrate_record(schema, record):

    return {**schema, **record}