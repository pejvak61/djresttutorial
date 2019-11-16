"""
User accounts Models!
"""
from django.db import models

class TblUserAccounts(models.Model):
    """
    User accounts model
    """
    uid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    alias_username = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user_accounts'
        ordering = ['uid']


class TblUserDetails(models.Model):
    """
    User account details model
    """
    detail_id = models.IntegerField(primary_key=True)
    useraccount = models.IntegerField()
    # pylint: disable=line-too-long
    # useraccount = models.ForeignKey(TblUserAccounts, on_delete=models.DO_NOTHING, related_name='TblUserAccounts.uid', db_column='useraccount')
    # pylint: disable=line-too-long
    # useraccount = models.ForeignKey(TblUserAccounts, models.DO_NOTHING, related_name='TblUserAccounts.uid')
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    birthdate = models.DateTimeField(blank=True, null=True)
    record_time = models.DateTimeField()
    creator = models.IntegerField()
    # pylint: disable=line-too-long
    # creator = models.ForeignKey(TblUserAccounts, on_delete=models.DO_NOTHING, related_name='TblUserAccounts.uid', db_column='creator')
    # pylint: disable=line-too-long
    # creator = models.ForeignKey(TblUserAccounts, models.DO_NOTHING, related_name='TblUserAccounts.uid', db_column='creator')

    class Meta:
        managed = False
        db_table = 'tbl_user_details'
        ordering = ['record_time']


class TblUserPassword(models.Model):
    """
    User passwords model
    """
    id_password = models.AutoField(primary_key=True)
    useraccount_id_pwd = models.IntegerField()
    # pylint: disable=line-too-long
    # useraccount_id_pwd = models.ForeignKey(TblUserAccounts, on_delete=models.DO_NOTHING, related_name='TblUserAccounts.uid', db_column='useraccount_id_pwd')
    # pylint: disable=line-too-long
    # useraccount_id_pwd = models.ForeignKey(TblUserAccounts, models.DO_NOTHING, related_name='TblUserAccounts.uid', db_column='useraccount_id_pwd')
    salt = models.CharField(max_length=200, blank=True, null=True)
    hash = models.CharField(max_length=200, blank=True, null=True)
    record_time = models.DateTimeField()
    creator = models.IntegerField()
    # pylint: disable=line-too-long
    # creator = models.ForeignKey(TblUserAccounts, on_delete=models.DO_NOTHING, related_name='TblUserAccounts.uid', db_column='creator')
    # pylint: disable=line-too-long
    # creator = models.ForeignKey(TblUserAccounts, models.DO_NOTHING, related_name='TblUserAccounts.uid', db_column='creator')

    class Meta:
        managed = False
        db_table = 'tbl_user_password'
        ordering = ['record_time']
