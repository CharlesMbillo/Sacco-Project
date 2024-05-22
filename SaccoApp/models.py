from django.db import models



class Member(models.Model):

    member_id = models.CharField(max_length=10)



class Transaction(models.Model):

    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    transaction_type = models.CharField(max_length=10)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    timestamp = models.DateTimeField(auto_now_add=True)

