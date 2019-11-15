"""
Snippet Models!
"""
from django.db import models


class TblUserAccounts(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    alias_username = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user_accounts'


class TblUserDetails(models.Model):
    detail_id = models.IntegerField(primary_key=True)
    useraccount = models.ForeignKey(TblUserAccounts, models.DO_NOTHING)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    birthdate = models.DateTimeField(blank=True, null=True)
    record_time = models.DateTimeField()
    creator = models.ForeignKey(TblUserAccounts, models.DO_NOTHING, db_column='creator')

    class Meta:
        managed = False
        db_table = 'tbl_user_details'


class TblUserPassword(models.Model):
    id_password = models.AutoField(primary_key=True)
    useraccount_id_pwd = models.ForeignKey(TblUserAccounts, models.DO_NOTHING, db_column='useraccount_id_pwd')
    salt = models.CharField(max_length=200, blank=True, null=True)
    hash = models.CharField(max_length=200, blank=True, null=True)
    record_time = models.DateTimeField()
    creator = models.ForeignKey(TblUserAccounts, models.DO_NOTHING, db_column='creator')

    class Meta:
        managed = False
        db_table = 'tbl_user_password'
